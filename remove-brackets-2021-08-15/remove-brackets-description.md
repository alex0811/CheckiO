Before solving this mission, you can try to solve the ["Brackets" ](https://py.checkio.org/mission/brackets/)mission.

Your task is to restore the balance of open and closed brackets by removing the unnecessary ones, while trying to use the minimum number of deletions.

Only 3 types of brackets (), [] and {} can be used in the given string.

Only a parenthesis can close a parenthesis. That is, in this expression "(}" - the brackets aren’t balanced. In an empty string, i.e., in a string that doesn’t contain any brackets - the brackets are balanced, but removing all of the brackets isn’t considered to be an optimal solution.

If there are more than one correct answer, then you should choose the one where the character that can be removed is closer to the beginning. For example, in this case "[(])", the correct answer will be "()", since the removable brackets are closer to the beginning of the line.

**Input:** A string of characters () {} []

**Output:** A string of characters () {} []

**Example:**

```python
remove_brackets('(()()') == '()()'
remove_brackets('[][[[') == '[]'
remove_brackets('[[(}]]') == '[[]]'
remove_brackets('[[{}()]]') == '[[{}()]]'
remove_brackets('[[[[[[') == ''
```

