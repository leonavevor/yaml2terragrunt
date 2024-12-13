---
title: REST API endpoints for admin stats
shortTitle: Admin stats
allowTitleToDifferFromFilename: true
intro: Use the REST API to retrieve a variety of metrics about your installation.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
  ghes: '*'
topics:
  - API
autogenerated: rest
---

{% ifversion ghes %}## About admin stats

These endpoints are only available to [authenticated](/rest/overview/authenticating-to-the-rest-api) site administrators. Normal users will receive a `404` response.

{% data reusables.user-settings.enterprise-admin-api-classic-pat-only %}{% elsif ghec %}{% data reusables.user-settings.enterprise-admin-api-classic-pat-only %}{% endif %}

<!-- Content after this section is automatically generated -->