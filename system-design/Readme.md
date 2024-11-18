# System Design

## Table of Contents
-   [Important Topics](#important-topics)
-   [Future Reads](#future-reads)
-   [Design Ticket Master](#ticket-master)
-   [Change Data Capture](#change-data-capture)
-   [Elastic Search](#elastic-search)
-   [Choke Point](#stratigies-for-handling-choke-point)

## Important Topics:
- `AWS Opensearch` - node query caching
from all of the clusters of elastic seach if cache 10k queries in LRU basis.
- Redis/Memcache
- `Long Polling`: Client open a connection which is there for 5-10 minutes. And keep waiting for servers response. Good for scenarios where client is not staying long on the page.
- `Web sockets`: Bidirectional persistent connection.
- `Server Sent Events`: SSE is unidirection, only from server to client.

<sub>[back to top](#table-of-contents)</sub>


## Future Reads:
https://www.hellointerview.com/blog/mastering-estimation

<sub>[back to top](#table-of-contents)</sub>


## Ticket Master

Hello Interview 
-   [Article](https://www.hellointerview.com/learn/system-design/answer-keys/ticketmaster) 

-   [Video](https://www.youtube.com/watch?v=fhdPyoO6aXI&list=PL5q3E8eRUieWtYLmRU3z94-vGRcwKr9tM)
-   [Excalidraw](https://app.excalidraw.com/l/56zGeHiLyKZ/2Z8PSPHfA8q)

<sub>[back to top](#table-of-contents)</sub>

## Change Data Capture
- It is a process in which changes to primary data store put onto stream and then those change events can be consumed and something can be done with them.

<sub>[back to top](#table-of-contents)</sub>

## Elastic Search
- For fast search queries, it uses a inverted index.
- It is not a good practice to use a elastic search as a primary database because of durability concerns and not support for complex transaction  management 

<sub>[back to top](#table-of-contents)</sub>

## Stratigies for handling Choke Point
- Using virtual queue.

<sub>[back to top](#table-of-contents)</sub>
