---
title: REST API endpoints for managing GitHub Enterprise Server
allowTitleToDifferFromFilename: true
shortTitle: Manage GHES
intro: >-
  Use the REST API to manage your {% data variables.product.product_name %}
  instance.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghes: '*'
topics:
  - API
autogenerated: rest
---

## About the Manage {% data variables.product.prodname_ghe_server %} API

You can manage {% data variables.location.product_location %} using the Manage {% data variables.product.prodname_ghe_server %} API. For example, you can retrieve information about the version of the {% data variables.product.prodname_ghe_server %} software running on the instance, or on instances with multiple nodes, view the status of replication.

{% ifversion management-console-manage-ghes-parity %}
> [!TIP] You can use this API to replace the functionality of the **Management Console API**, which was removed in {% data variables.product.prodname_ghe_server %} version 3.15. For a mapping between the endpoints, see {% ifversion ghes > 3.14 %}"[AUTOTITLE](/enterprise-server@3.14/rest/enterprise-admin/management-console)" in version 3.14 of the documentation.{% else %}"[AUTOTITLE](/rest/enterprise-admin/management-console)."{% endif %}
{% endif %}

Specify the port number when making API calls to endpoints for the Manage {% data variables.product.prodname_ghe_server %} API. If your instance uses TLS, the port number is 8443. Otherwise, the port number is 8080. If you cannot provide a port number, you'll need to configure your client to automatically follow redirects. For more information, see "[AUTOTITLE](/admin/configuration/configuring-network-settings/configuring-tls)."

You can also use the {% data variables.product.prodname_ghe_server %} extension of the {% data variables.product.prodname_cli %} to invoke endpoints in the Manage {% data variables.product.prodname_ghe_server %} API. For more information, see the [`github/gh-es`](https://github.com/github/gh-es/blob/main/README.md) repository.

### Authentication

To authenticate requests to endpoints for the Manage {% data variables.product.prodname_ghe_server %} API, specify the password for the instance's root site administrator account as an authentication token. Use standard HTTP authentication to send the password. The `api_key` user identifies the root site administrator. The following example demonstrates authentication for this API. Replace ROOT-SITE-ADMINISTRATOR-PASSWORD with the password, and ADMINISTRATION-PORT with either 8443 or 8080.

```shell
curl -L -u "api_key:ROOT-SITE-ADMINISTRATOR-PASSWORD" 'http(s)://HOSTNAME:ADMINISTRATION-PORT/manage'
```

{% ifversion enterprise-management-console-multi-user-auth %}

### Authentication as a {% data variables.enterprise.management_console %} user

{% data variables.enterprise.management_console %} user accounts can also authenticate to access these endpoints. For more information, see "[AUTOTITLE](/admin/configuration/administering-your-instance-from-the-management-console/managing-access-to-the-management-console#management-console-user)."

To authenticate with the password for a {% data variables.enterprise.management_console %} user account, use standard HTTP authentication. In the following example, replace YOUR_USER_NAME and YOUR_PASSWORD with the account's user name and password.

```shell
curl -L -u "YOUR_USER_NAME:YOUR_PASSWORD" 'http(s)://HOSTNAME:ADMINISTRATION-PORT/manage'
```

{% endif %}

### Query parameters

By default, the response includes information from about all configured nodes for the instance. On an instance with multiple nodes, the details originate from `/data/user/common/cluster.conf`. You can use the following query parameters to filter the response for information about specific nodes.

| Query parameter | Description |
| :- | :- |
| `uuid` | Unique identifier for the node. |
| `cluster_role` | For nodes in a cluster, the roles that apply to the node. For more information, see "[AUTOTITLE](/admin/enterprise-management/configuring-clustering/about-cluster-nodes)." |

You can specify multiple values for the query parameter by delimiting the values with a comma. For example, the following request uses curl to return any nodes with the `web-server` or `storage-server` role.

```shell
curl -L -u "api_key:ROOT-SITE-ADMINISTRATOR-PASSWORD" 'http(s)://HOSTNAME:ADMINISTRATION-PORT/manage/v1/config/nodes?cluster_role=WebServer,StorageServer'
```

<!-- Content after this section is automatically generated -->