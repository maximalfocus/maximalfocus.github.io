---
title: "Design Pastebin.com (or Bit.ly)"
date: 2025-11-09
type: post
tags:
  - pastebin
  - system-design
  - aac
---

### Design Pastebin.com (or Bit.ly)

```mermaid
C4Container
    Person(client, "Anonymous User")

    System_Ext(dns, "DNS", "Resolves domain name")
    System_Ext(cdn, "CDN", "Serves and caches static assets")

    Container_Boundary(pastebin_system, "Pastebin.com") {
        Container(load_balancer, "Load Balancer", "Nginx", "Distributes incoming traffic")
        Container(web_servers, "Web Servers", "Reverse Proxy", "Horizontally scaled application servers")
        
        %% Grouping APIs and their immediate cache together
        Container_Boundary(api_layer, "API Layer") {
          Container(write_api, "Write API", "API Application", "Handles paste creation")
          Container(read_api, "Read API", "API Application", "Handles paste viewing")
          Container(memory_cache, "Memory Cache", "Redis/Memcached", "Caches frequently accessed pastes")
        }

        %% Placing databases directly below the API layer that consumes them
        Container_Boundary(database_layer, "Databases") {
            ContainerDb(sql_master, "SQL Master", "SQL Database", "Handles all write operations")
            ContainerDb(sql_replicas, "SQL Replicas", "SQL Database", "Handles read queries for paste metadata")
            ContainerDb(object_store, "Object Store", "Amazon S3", "Stores the raw paste content")
        }
        
        %% Analytics is a separate concern
        Container(analytics, "Analytics Service", "MapReduce", "Processes logs for analytics")
        ContainerDb(sql_analytics, "Analytics DB", "Data Warehouse", "Stores aggregated analytics data")
    }

    %% -- User Request Flow --
    Rel(client, dns, "1. Resolves pastebin.com", "DNS Query")
    Rel(client, cdn, "2. Requests static content", "HTTPS")
    Rel(client, load_balancer, "3. Sends API request", "HTTPS")
    Rel(load_balancer, web_servers, "4. Forwards request")

    %% -- Write Path (Cleanly separated) --
    Rel(web_servers, write_api, "5a. Forwards write request")
    Rel(write_api, sql_master, "6a. Writes metadata")
    Rel(write_api, object_store, "6b. Writes paste content")
    
    %% -- Read Path (Showing full cache-aside logic) --
    Rel(web_servers, read_api, "5b. Forwards read request")
    Rel(read_api, memory_cache, "6c. Checks cache for paste")
    Rel(read_api, sql_replicas, "7a. On miss, reads metadata")
    Rel(read_api, object_store, "7b. On miss, reads paste content")
    Rel(read_api, memory_cache, "8. Writes new data to cache")

    %% -- Analytics Flow --
    Rel(web_servers, analytics, "Sends logs for processing")
    Rel(analytics, sql_analytics, "Stores aggregated results")
    Rel(sql_master, sql_replicas, "Replicates data")
```

### Deployment Diagram for Pastebin on AWS

```mermaid
graph TD
    %% Styling for clarity
    classDef aws fill:#FF9900,stroke:#333,stroke-width:2px;
    classDef az fill:#F3F3F3,stroke:#555,stroke-width:1px,color:#333;
    classDef eks fill:#232F3E,stroke:#fff,stroke-width:1px,color:#fff;
    classDef pod fill:#4A5B70,stroke:#fff,stroke-width:0px,color:#fff;
    classDef db fill:#3E6B47,stroke:#fff,stroke-width:1px,color:#fff;
    classDef ext fill:#999,stroke:#333,stroke-width:1px,color:#fff;

    %% --- External Systems ---
    subgraph The Internet
        client_device("User's Device<br/><i>Web Browser</i>")
        route53("Route 53<br/><i>DNS</i>")
        cloudfront("CloudFront<br/><i>CDN</i>")
    end

    %% --- AWS Cloud ---
    subgraph aws_cloud["AWS Cloud"]
        subgraph us-east-1 Region
            alb("Application<br/>Load Balancer")

            subgraph availability_zone_a["Availability Zone A"]
                subgraph eks_a ["EKS Cluster A"]
                    web_a("Pod: Web Server")
                    read_a("Pod: Read API")
                    write_a("Pod: Write API")
                end
                rds_master("RDS Master<br/><i>PostgreSQL</i>")
                cache_a("ElastiCache<br/><i>Redis Node</i>")
            end

            subgraph availability_zone_b["Availability Zone B"]
                subgraph eks_b ["EKS Cluster B"]
                    web_b("Pod: Web Server")
                    read_b("Pod: Read API")
                    write_b("Pod: Write API")
                end
                rds_replica("RDS Replica<br/><i>PostgreSQL</i>")
                cache_b("ElastiCache<br/><i>Redis Node</i>")
            end

            s3("Amazon S3<br/><i>Object Storage & Logs</i>")
            emr("EMR Cluster<br/><i>Analytics</i>")
            redshift("Redshift<br/><i>Data Warehouse</i>")
        end
    end

    %% --- Relationships ---
    client_device -- "1. DNS Query" --> route53
    route53 -- "2. Returns IP" --> client_device
    client_device -- "3. Requests Static Assets" --> cloudfront
    client_device -- "4. API Requests" --> alb

    alb --> web_a & web_b

    web_a --> read_a & write_a
    web_b --> read_b & write_b

    write_a --> rds_master & s3
    read_a & read_b --> cache_a & cache_b
    read_a & read_b -- "On Cache Miss" --> rds_replica & s3

    rds_master -- "Replication" --> rds_replica
    cloudfront -- "Pulls Origin" --> s3
    
    web_a & web_b -- "Writes Logs" --> s3
    emr -- "Reads Logs" --> s3
    emr -- "Writes Aggregates" --> redshift

    %% --- Apply Styling ---
    class client_device,route53,cloudfront ext;
    class aws_cloud aws;
    class eks_a,eks_b eks;
    class web_a,web_b,read_a,read_b,write_a,write_b,alb,emr pod;
    class rds_master,rds_replica,cache_a,cache_b,s3,redshift db;
    class availability_zone_a,availability_zone_b az;
```

Source:

- [Design Pastebin.com (or Bit.ly)](https://github.com/maximalfocus/system-design-primer/blob/master/solutions/system_design/pastebin/README.md)
- [C4 Diagrams](https://github.com/mermaid-js/mermaid/edit/develop/packages/mermaid/src/docs/syntax/c4.md)
