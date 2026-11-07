#!/usr/bin/env python3
"""Duplicate defect finder: TF-IDF text similarity over defect reports.

Usage:
    python3 duplicate_finder.py defects.csv
    python3 duplicate_finder.py defects.csv "text of the new report"

Duplicate defects are the quiet tax on a QA team: the same bug filed
three times gets triaged three times. This tool turns a defect log
into vectors (term frequency times inverse document frequency) and
ranks existing defects by cosine similarity to a new report, so the
human decides in seconds whether it is a duplicate. It ranks; the
tester still makes the call.
"""

import csv
import math
import re
import sys
from collections import Counter

TOKEN = re.compile(r"[a-z0-9']+")
LIKELY_DUPLICATE = 0.45


def tokenize(text):
    return TOKEN.findall(text.lower())


class TfidfIndex:
    def __init__(self, docs):
        self.docs = docs
        self.doc_count = len(docs)
        doc_freq = Counter()
        self.term_freqs = []
        for _doc_id, text in docs:
            counts = Counter(tokenize(text))
            self.term_freqs.append(counts)
            for term in counts:
                doc_freq[term] += 1
        self.idf = {
            term: math.log((self.doc_count + 1) / (freq + 1)) + 1
            for term, freq in doc_freq.items()
        }
        self.vectors = [self._vectorize(counts) for counts in self.term_freqs]

    def _vectorize(self, counts):
        return {term: count * self.idf.get(term, 1.0) for term, count in counts.items()}

    @staticmethod
    def _cosine(left, right):
        shared = set(left) & set(right)
        dot = sum(left[t] * right[t] for t in shared)
        norm_l = math.sqrt(sum(v * v for v in left.values()))
        norm_r = math.sqrt(sum(v * v for v in right.values()))
        if norm_l == 0 or norm_r == 0:
            return 0.0
        return dot / (norm_l * norm_r)

    def rank(self, text, top=3):
        query = self._vectorize(Counter(tokenize(text)))
        scored = [
            (self._cosine(query, vector), self.docs[i][0])
            for i, vector in enumerate(self.vectors)
        ]
        return sorted(scored, reverse=True)[:top]


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 duplicate_finder.py <defects.csv> [new report text]")
        return 2
    with open(sys.argv[1], newline="") as handle:
        rows = list(csv.DictReader(handle))
    docs = [(r["id"], r["title"] + " " + r["description"]) for r in rows]
    titles = {r["id"]: r["title"] for r in rows}
    index = TfidfIndex(docs)
    demos = [
        "The reset password link works more than once after being used",
        "Charts take a long time to load on slow connections",
    ]
    targets = [sys.argv[2]] if len(sys.argv) > 2 else demos
    print(f"Indexed defects: {len(docs)}")
    for text in targets:
        print(f"\nNew report: {text}")
        for score, doc_id in index.rank(text):
            verdict = "LIKELY DUPLICATE" if score >= LIKELY_DUPLICATE else "possible relation"
            print(f"  {score:.2f}  {doc_id}  {titles[doc_id]}  ({verdict})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
