# Random lock puzzles, their answers, and input format.
import random


# The save format stores each puzzle's numbers in this order.
LockPuzzleKeys = ("bucket_num", "bucket_divisor", "claw_num", "claw_divisor",
                  "mirror_left", "mirror_right", "num1", "num2")


# Calculate tag values from the same numbers that appear on the clue sheets.
def LockValues(Puzzle):
    Bucket = Puzzle["bucket_num"] % Puzzle["bucket_divisor"]
    Claw = Puzzle["claw_num"] // Puzzle["claw_divisor"]
    Mirror = Puzzle["mirror_left"] * Puzzle["mirror_right"]
    if Bucket < Claw:
        Door = (Puzzle["num1"] + Puzzle["num2"]) % 10
    else:
        Door = (Puzzle["num1"] - Puzzle["num2"]) % 10
    return {"Bucket": Bucket, "Claw": Claw, "Mirror": Mirror, "Door": Door}


# Choose small arithmetic expressions with four distinct single-digit results.
def NewLockPuzzle():
    while True:
        BucketDivisor = random.randint(2, 10)
        ClawDivisor = random.randint(2, 9)
        MirrorLeft, MirrorRight = random.choice([(2, 2), (2, 3), (3, 2), (2, 4), (4, 2), (3, 3)])
        Puzzle = {"bucket_num": random.randint(10, 99), "bucket_divisor": BucketDivisor,
                  "claw_num": random.randint(0, 10 * ClawDivisor - 1), "claw_divisor": ClawDivisor,
                  "mirror_left": MirrorLeft, "mirror_right": MirrorRight,
                  "num1": random.randint(20, 49), "num2": random.randint(10, 19)}
        Values = LockValues(Puzzle)
        # Multiples of 5 make the addition and subtraction branches equal modulo 10.
        if len(set(Values.values())) == 4 and Puzzle["num2"] % 5 != 0:
            return Puzzle


# Maintenance order is Claw, Mirror, Bucket, Door; the visible slots run in reverse.
def LockCode(Game):
    Values = LockValues(Game["LockPuzzle"])
    return "".join(str(Values[Tag]) for Tag in ("Door", "Bucket", "Mirror", "Claw"))


# Accept exactly four ASCII digits, rejecting all other characters and lengths.
def ValidCode(Code):
    if len(Code) != 4:
        return False
    for Character in Code:
        if Character not in "0123456789":
            return False
    return True
