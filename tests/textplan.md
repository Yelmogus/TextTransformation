# Text Transformation
Text Transformation
LargeScale Programming Fall 2019 Rensselaer Polytechnic Institute Project

Name follows the format: GivenX_WhenFunction_ThenResult

| Test Number | Input | Expected Output | Name | Description |
|:-----------|:-----:|:---------------:|:----:|:-----------|
| 0 | {
  "type": "html",
  "data": "<h1> hello world </h1>",
  "transformations": {
    "stripped": true,
    "grams": [1,2]
    "title": true
   },
} | None | GivenNull_WhenHandleRequest_ThenReturnNull  | Testing valid inputs |
| 1 | Input Value Missing Values  | BadRequest | GivenIllFormat_WhenHandleRequest_ThenReturnError | Testing invalid inputs

- [x] Examine code
- [ ] Commit fixes
- [ ] Request a review
