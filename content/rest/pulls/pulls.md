---
title: REST API endpoints for pull requests
shortTitle: Pull requests
allowTitleToDifferFromFilename: true
intro: Use the REST API to interact with pull requests.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
topics:
  - API
autogenerated: rest
---

## About pull requests

You can list, view, edit, create, and merge pull requests using the REST API. For information about how to interact with comments on a pull request, see "[AUTOTITLE](/rest/issues/comments)."

Pull requests are a type of issue. Any actions that are available in both pull requests and issues, like managing assignees, labels, and milestones, are provided by the REST API to manage issues. For more information, see "[AUTOTITLE](/rest/issues)."

### Link Relations

Pull requests have these possible link relations:

* `self`: The API location of this pull request
* `html`: The HTML location of this pull request
* `issue`: The API location of this pull request's [issue](/rest/issues)
* `comments`: The API location of this pull request's [issue comments](/rest/issues/comments)
* `review_comments`: The API location of this pull request's [review comments](/rest/pulls/comments)
* `review_comment`: The [URL template](/rest/using-the-rest-api/getting-started-with-the-rest-api#hypermedia) to construct the API location for a [review comment](/rest/pulls/comments) in this pull request's repository
* `commits`: The API location of this pull request's [commits](#list-commits-on-a-pull-request)
* `statuses`: The API location of this pull request's [commit statuses](/rest/commits#commit-statuses), which are the statuses of its `head` branch

<!-- Content after this section is automatically generated -->