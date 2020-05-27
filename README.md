# Django-Todolist

Followed Dennis Ivy's tutorial https://youtu.be/pLN-OnXjOJg (source code at https://github.com/divanov11/to-do-app), excluding the styling component.
Wanted to practice by personalizing and customizing different functionalities and styling components.

## Edits:
1. Added due date
2. Added style using Materialize CSS

## Problems I Ran into in the Process:
Using Materialize CSS, form rendering don't sync well.
To resolve the issue with BooleanField:

```
[type="checkbox"]:not(:checked), [type="checkbox"]:checked {
    position: static!important;
    left: 0px!important;
    opacity: 1!important;
    visibility: visible!important;
    pointer-events: all!important;
}
```

were added to style at the head of base.html
(solution provided by grekpg from https://github.com/Dogfalo/materialize/issues/1376)
