
"""
https://groupprops.subwiki.org/wiki/Symmetric_group:S4#Table_classifying_subgroups_up_to_automorphisms
"""

all_s4_subgroups = {
    "C2_single_transposition": {
        "order": 2,
        "copies": 6,
        "generators": [
            [(1, 0, 2, 3)], #1 (0 1)
            [(2, 1, 0, 3)], #2 (0 2)
            [(3, 1, 2, 0)], #3 (0 3)
            [(0, 2, 1, 3)], #4 (1 2)
            [(0, 3, 2, 1)], #5 (1 3)
            [(0, 1, 3, 2)] #6 (2 3)
        ]
    },
    "C2_double_transposition": {
        "order": 2,
        "copies": 3,
        "generators": [
            [(1, 0, 3, 2)], #1
            [(3, 2, 1, 0)], #2
            [(2, 3, 0, 1)] #3
        ]
    },
    "K4_normal": {
        "order": 4,
        "copies": 1,
        "generators": [
            [(1, 0, 3, 2), (3, 2, 1, 0)]
        ]
    },

    "K4_nonnormal": {
        "order": 4,
        "copies": 3,
        "generators": [
            [(0, 1, 3, 2), (1, 0, 2, 3)],
            [(3, 1, 2, 0), (0, 2, 1, 3)],
            [(2, 1, 0, 3), (0, 3, 2, 1)]
        ]
    },
    "A3": {
        "order": 3,
        "copies": 4,
        "generators": [
            [(0, 3, 1, 2)], # fix 0
            [(3, 1, 0, 2)], # fix 1
            [(3, 0, 2, 1)], # fix 2
            [(2, 0, 1, 3)] # fix 3
        ]
    },
    "C4": {
        "order": 4,
        "copies": 3,
        "generators": [
            [(3, 0, 1, 2)],
            [(2, 3, 1, 0)],
            [(2, 0, 3, 1)]
        ]
    },
    "S3": {
        "order": 6,
        "copies": 4,
        "generators": [
            [(0, 2, 1, 3), (0, 3, 2, 1)], # fix 0
            [(2, 1, 0, 3), (3, 1, 2, 0)], # fix 1
            [(1, 0, 2, 3), (3, 1, 2, 0)], # fix 2
            [(1, 0, 2, 3), (2, 1, 0, 3)] # fix 3
        ]
    },
    "D8": {
        "order": 8,
        "copies": 3,
        "generators": [
            [(1, 2, 3, 0), (0, 3, 2, 1)],
            [(1, 3, 0, 2), (0, 2, 1, 3)],
            [(2, 3, 1, 0), (0, 1, 3, 2)]
        ]
    },
    "A4": {
        "order": 12,
        "copies": 1,
        "generators": [
            [(1, 0, 3, 2), (2, 0, 1, 3)]

        ]
    }
}
