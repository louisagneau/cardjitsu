# 🃏 Card-Jitsu (OOP Practice)

This is a small project to **learn and practice Object-Oriented Programming (OOP)** in Python using a simple, turn-based card game inspired by Card-Jitsu (Club Penguin).

---

## Purpose

The goal is to understand how to:

- Define and use **classes**
- Create and manipulate **objects**
- Use methods like `__init__()`, `__str__()`, and custom logic.

---

## Game Logic

Each `Card` has:
- a `name` (just flavor text),
- a `power` (1–10),
- an `element`: `fire`, `water`, or `snow`.

Rules:
- Fire beats Snow  
- Snow beats Water  
- Water beats Fire  
- If same element → higher power wins  
- If tied → it's a tie

---

## Files

- `card.py` — defines the `Card` class and a basic list of cards
- `play.py` — simulates a random game (best of 3)

---

## How to Run

From the folder:

```bash
python3 play.py
```

