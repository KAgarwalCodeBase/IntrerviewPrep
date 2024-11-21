# System Design

## Table of Contents
-   [Important Topics](#important-topics)
    - [AWS Opensearch](#aws-opensearch)
    - [Redis/Memcache](#redismemcache)
    - [Long Polling](#long-polling)
    - [Web Sockets](#web-sockets)
    - [Server Sent Events](#server-sent-events-sse)
    - [Change Data Capture](#change-data-capture)
    - [Elastic Search](#elastic-search)
    - [Choke Point](#stratigies-for-handling-choke-point)
    - [Secondary Indexes in Dynamo DB](#secondary-indexes-in-dynamo-db)
-   [Future Reads](#future-reads)
-   [Delivery Framework](#delivery-framework)
-   [Core Concepts](#core-concepts)
-   [Design Ticket Master](#design-ticket-master)
-   [Design Uber](#design-uber)

## Important Topics:
### AWS Opensearch 
Node query caching from all of the clusters of elastic seach if cache 10k queries in LRU basis.

<sub>[back to top](#table-of-contents)</sub>

### Redis/Memcache

<sub>[back to top](#table-of-contents)</sub>

### Long Polling
Client open a connection which is there for 5-10 minutes. And keep waiting for servers response. Good for scenarios where client is not staying long on the page.

If you need to give your clients near-realtime updates, you'll need a way for the clients to receive updates from the server. Long polling is a great way to do this that blends the simplicity and scalability of HTTP with the realtime updates of Websockets. With long polling, the client makes a request to the server and the server holds the request open until it has new data to send to the client. Once the data is sent, the client makes another request and the process repeats. Notably, you can use standard load balancers and firewalls with long polling - no special infrastructure needed.

<sub>[back to top](#table-of-contents)</sub>

### Web sockets
Bidirectional persistent connection.

<sub>[back to top](#table-of-contents)</sub>

### Server Sent Events (SSE)
SSE is unidirection, only from server to client.

 Server Sent Events (SSE) are a great way to send updates from the server to the client. They're similar to long polling, but they're more efficient for unidirectional communication from the server to the client. SSE allows the server to push updates to the client whenever new data is available, without the client having to make repeated requests as in long polling. This is achieved through a single, long-lived HTTP connection, making it more suitable for scenarios where the server frequently updates data that needs to be sent to the client. Unlike Websockets, SSE is designed specifically for server-to-client communication and does not support client-to-server messaging. This makes SSE simpler to implement and integrate into existing HTTP infrastructure, such as load balancers and firewalls, without the need for special handling.

<sub>[back to top](#table-of-contents)</sub>

### Change Data Capture
- It is a process in which changes to primary data store put onto stream and then those change events can be consumed and something can be done with them.

<sub>[back to top](#table-of-contents)</sub>

### Elastic Search
- For fast search queries, it uses a inverted index.
- It is not a good practice to use a elastic search as a primary database because of durability concerns and not support for complex transaction  management 

<sub>[back to top](#table-of-contents)</sub>

### Choke Point
- Using virtual queue.

### [Secondary Indexes in Dynamo DB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html)
A secondary index is a data structure that contains a subset of attributes from a table, along with an alternate key to support Query operations. You can retrieve data from the index using a Query, in much the same way as you use Query with a table. A table can have multiple secondary indexes, which give your applications access to many different query patterns.

<sub>[back to top](#table-of-contents)</sub>


## Future Reads:
https://www.hellointerview.com/blog/mastering-estimation
-   
-   API Gateway  
-   SSL Termination  
-   Authentication  
-   Load balancing  
-   Routing   
-   Rate Limiting  
-   Notification Service(Apple push notification, google android firebase)  
-   B-Trees: (It is optimised for single dimension data queries not a two dimensional data queries). As we required to search for driver on the basis of it's [lat, long] position so SQL DB's are not good choice because they internally uses B-Tree.
- Geospatial Index, Quadtree, [PostGIS](https://postgis.net/) 
![QuadTree](./assets/quad-tree.png)
    -   Good when it is unevenly distribution of density.
    -   Fewer updates because we do not want to reindex the tree every time. 

- Redis GeoHashing
    ![Geohasing](./assets/geohashing.png)
    - Good for high number of writes.
    - less good for unevenly distribution.
-  Fan-out
- gRPC (Google Remote Procedure Call)
- Message Broker

<sub>[back to top](#table-of-contents)</sub>

## [Delivery Framework](https://www.hellointerview.com/learn/system-design/in-a-hurry/delivery)
-   Requirements (~ 5 mins)
    -   Functional Requirements
    -   Non-Functional Requirements
    -   Capacity Estimation
-   Core Entities (~ 2 mins)
-   API or System Interface (~5 minutes)
-   [Optional] Data Flow (~5 minutes)  
-   High Level Design (~10-15 minutes)
-   Deep Dives (~10 minutes)

<sub>[back to top](#table-of-contents)</sub>

## [Core Concepts](https://www.hellointerview.com/learn/system-design/in-a-hurry/core-concepts)
-   Scaling [Horizontal / Vertical]
-   Work Distribution [Load Balancer]
-   Data Distribution [Sharding]
-   Consistency [Strong / Week / Eventual]
-   Locking [Granularity / Duration / Can we bypass]
-   Indexing [Primary / Secondary / Specialized]
-   Communication Protocols [Internal - HTTP(s), gRPC / External - HTTP(S), SSE or long polling, and Websockets]

## Design Ticket Master

Hello Interview 
-   [Article](https://www.hellointerview.com/learn/system-design/answer-keys/ticketmaster) 
-   [Video](https://www.youtube.com/watch?v=fhdPyoO6aXI&list=PL5q3E8eRUieWtYLmRU3z94-vGRcwKr9tM)
-   [Excalidraw](https://app.excalidraw.com/l/56zGeHiLyKZ/2Z8PSPHfA8q)

<sub>[back to top](#table-of-contents)</sub>


## Design Uber
-   [Article](https://www.hellointerview.com/learn/system-design/answer-keys/uber)
-   [Video](https://www.youtube.com/watch?v=lsKU38RKQSo&list=PL5q3E8eRUieWtYLmRU3z94-vGRcwKr9tM&index=2&ab_channel=HelloInterview-SWEInterviewPreparation)
-   [Excalidraw](https://app.excalidraw.com/l/56zGeHiLyKZ/6WXHvJ2vXSd)


### Location DB (For Driver's Location)
-   As we required to search for driver on the basis of it's [lat, long] position so SQL DB's are not good choice because they internally uses B-Tree.

<sub>[back to top](#table-of-contents)</sub>

## Design Dropbox
Pattern Trust but Verify: Instead of trusting on client that it is always sending a correct data do check as much as possible.

