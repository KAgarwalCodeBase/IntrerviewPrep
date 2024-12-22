# System Design

## Table of Contents
-   [Important Topics](#important-topics)
    - [CAP Theorem](#cap-theorem)
    - [Consistent Hashing](#consistent-hashing)
    - [Bloom Filter](#bloom-filter)
    - [AWS Opensearch](#aws-opensearch)
    - [Redis](#redis)
    - [Kafka](#kafka)
    - [Cassandra](#cassandra)
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
-   [Key Technologies](#key-technologies)
-   [Design Ticket Master](#design-ticket-master)
-   [Design Uber](#design-uber)

Flink/Aws firehouse / Spark streams: Aggregator services 
count min sketch / map reduce 

## Important Topics:

### [CAP Theorem](https://en.wikipedia.org/wiki/CAP_theorem)
**Strong consistency**
- implement distributed transactions
- limit to a single node
- discuss consensus protocols
- accept higher latency
- Example tools
    - PostgreSQL
    - Trad RDBMS
    - Spanner
    - NoSQL with strong consistency mode (DynamoDB)



**Availability**
- use multiple replicas
- CDC and eventual consistency is ok
- Example tools
    - DynamoDB (in multi-AZ mode)
    - Cassandra

#### Different types of consistency
1. Strong Consistency: all reads reflect most recent write
2. Causal Consistency: related events appear in order
3. Read-your-writes Consistency: user sees their own updates
4. Eventual Consistency: updates will propagate eventually

<sub>[back to top](#table-of-contents)</sub>

### [Consistent Hashing](https://www.youtube.com/watch?v=zaRkONvyGr8)
Consistent hashing is a fundamental technique used in distributed systems to partition data / load across machines in a way that prioritizes evenness of distribution while minimizing re-mapping of data if a node enters or leaves the system.

<sub>[back to top](#table-of-contents)</sub>

### [Bloom filter](https://www.youtube.com/watch?v=gBygn3cVP80)
A Bloom filter is a space-efficient probabilistic data structure used to test whether an element is a member of a set. It is designed for scenarios where fast lookups and memory efficiency are crucial, but it allows for a small probability of false positives.

<sub>[back to top](#table-of-contents)</sub>


### AWS Opensearch 
Node query caching from all of the clusters of elastic seach if cache 10k queries in LRU basis.

<sub>[back to top](#table-of-contents)</sub>

### [Redis](https://www.youtube.com/watch?v=fmT5nlEkl3U&list=PL5q3E8eRUieUHnsz0rh0W6AzwdVJBwEK6&index=2&pp=iAQB)
Where to use Redis:
- ⁠basic rate limiting
- ⁠⁠geo spacitial index
- ⁠⁠service registry
- ⁠⁠producer-consumer i.e async job queue

**Redis stream** - order of list of items that given an id which is usually a timestamp this id’s has their own key- value pair.


- Data structures database
- Redis give us power to use data structures in databases.
- Bloomfilter, string, obj might be Redis key  
- Replica of Redis updated every minute.  
- Only way to shard the Redis is to choose the key on which we are going to shard the data.
- Hotkey problem: append random number to the key.
- To scale Redis thought about key space.

<sub>[back to top](#table-of-contents)</sub>

### [Kafka](https://www.youtube.com/watch?v=DU8o-OTeoCc&list=PL5q3E8eRUieUHnsz0rh0W6AzwdVJBwEK6&index=1&pp=iAQB)
Use case: 
- Multiple consumer. ex: Facebook Comments.
- Inorder message processing. ex: Ticketmaster.
- In place of queue. ex: YouTube transcribe.
- Decouple producer and consumer so they can scale independently. ex: Leetcode online judge. 
- Need to process a lot of data in realtime. ex: Ad-click
- Kafka will do the implicit retry at producer side.
- Kafka does not do implicit retry at consumer side we need to do it and put the message in retry queue.

<sub>[back to top](#table-of-contents)</sub>

### [Cassandra](https://www.hellointerview.com/learn/system-design/deep-dives/cassandra)

**Data Model**  
Keyspaces->Table->Row->Column

**Partition Key** - One or more columns that are used to determine what partition the row is in. We'll discuss partitioning of data later in this deep-dive.  
**Clustering Key** - Zero or more columns that are used to determine the sorted order of rows in a table. Data ordering is important depending on one's data modeling needs, so Cassandra gives users control over this via the clustering keys.

**Partitioning**  
- Uses consistent hashing  

**Replication**
- NetworkTopologyStrategy
- SimpleStrategy.

**Consistency**  
- Cassandra does not support any notions of ACID gurantees.
- It only supports atomic and isolated writes at the row level in partition.
- Cassandra supports different consistency level.
example: one, two, three, quorum, any etc.
- One notable consistency level to understand is QUORUM. QUORUM requires a majority (n/2 + 1) of replicas to respond. Applying QUORUM to both reads and writes guarantees that writes are visible to reads because at least one overlapping node is guaranteed to participate in both a write and a read. 

**Storage Model**
- Cassandra Uses Log Structured Merge (LSM) Tree. The 3 constructs core to the LSM tree index are:
- Commit Log - This basically is a write-ahead-log to ensure durability of writes for Cassandra nodes.
- Memtable - An in-memory, sorted data structure that stores write data. It is sorted by primary key of each row.
- SSTable - A.k.a. "Sorted String Table." Immutable file on disk containing data that was flushed from a previous Memtable.
![Write in Cassandra](./assets/storage_cassandra.png)

- When reading data for a particular key, Cassandra reads the Memtable first, which will have the latest data. If the Memtable does not have the data for the key, Cassandra leverages a bloom filter to determine which SSTables on disk might have the data. It then reads the SSTables in order from newest to oldest to find the latest data for the row. 

**Falut Tolerance**  
Nodes independently detect failures during gossip, temporarily storing write data as hints for offline nodes to ensure data consistency and recovery when they rejoin the cluster.

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

### [Elastic Search](https://www.youtube.com/watch?v=PuZvF2EyfBM&list=PL5q3E8eRUieUHnsz0rh0W6AzwdVJBwEK6&index=3)

- For fast search queries, it uses a inverted index.
- Elastic search support point in time search.
-  A search request by default executes against the most recent visible data of the target indices, which is called point in time. Elasticsearch pit (point in time) is a lightweight view into the state of the data as it existed when initiated.
- It is very expensive.  

**Question:** How you can use elastic search in your system design interview?  
**Answer:** For complex search   
- geo sptial.
- vector search.
- full text search.

Notes:
- Not your primary database.  
- Best with read-heavy workloads.   
- Must tolerate eventual consistency. 
- Denormalization is the key. (It faces problems in join. So, not good for things which required join.)  
- Do you even need it.


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

<sub>[back to top](#table-of-contents)</sub>

## Key Technologies
- Core Database (DynamoDB, MongoDB)
    - Relational Databases
    - NoSQL Databases
- Blob Storage (Amazon S3, Google Cloud Storage)
- Search Optimized Database (Elasticsearch)
- API Gateway (AWS API Gateway, Kong and Apigee.)
- Load Balancer (AWS Elastic Load Balancer, NGINX and HAProxy)
- Queue (Kafka and SQS) 
- Streams / Event Sourcing (Kafka and Kinesis)
- Distributed Lock (Redis or Zookeeper)
- Distributed Cache (Redis and Memcached)
- CDN (Cloudflare, Akamai and Amazon CloudFront)

<sub>[back to top](#table-of-contents)</sub>

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

