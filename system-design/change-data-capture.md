## Change Data Capture
Change Data Capture (CDC) is a technique used in database and data integration systems to identify and track changes made to the data in a primary data store. These changes are captured as events and can be processed in real-time or near real-time for various downstream applications. Here's a breakdown of CDC:

### Key Concepts:
1. **Source Data Store**:
   - The database or data system where the original data resides (e.g., relational databases like MySQL, PostgreSQL, Oracle, or NoSQL systems like MongoDB).

2. **Change Events**:
   - Any modifications made to the data, such as `INSERT`, `UPDATE`, or `DELETE` operations, are detected and transformed into structured events.

3. **Streaming Changes**:
   - These change events are published to a stream (e.g., Apache Kafka, AWS Kinesis) or a message queue for further processing.

4. **Consumers**:
   - Applications or systems that subscribe to the stream of change events to perform actions, such as updating downstream databases, triggering workflows, syncing data, or feeding analytics systems.

---

### Why Use CDC?
1. **Real-Time Data Processing**:
   - Enables real-time data synchronization across systems without the need for bulk data transfers.

2. **Event-Driven Architecture**:
   - Facilitates the implementation of event-driven applications and workflows.

3. **Efficiency**:
   - Reduces the overhead of full-table scans or periodic bulk updates by processing only the changes.

4. **Scalability**:
   - Supports large-scale systems where constant replication or data synchronization is required.

---

### CDC Methods:
1. **Log-Based CDC**:
   - Reads changes directly from the database transaction log (e.g., MySQL binlog, PostgreSQL WAL).
   - Efficient and minimally intrusive.

2. **Trigger-Based CDC**:
   - Uses database triggers to log changes into a separate table.
   - May have performance impacts on the source database.

3. **Query-Based CDC**:
   - Periodically queries the source database to detect changes (e.g., using timestamps).
   - Simpler but less efficient for high-change systems.

4. **Hybrid Approaches**:
   - Combines multiple CDC methods for optimized performance and reliability.

---

### Popular Tools for CDC:
1. **Debezium**:
   - Open-source CDC tool for databases like MySQL, PostgreSQL, MongoDB, and others.

2. **Amazon Database Migration Service (DMS)**:
   - AWS solution for CDC and data migration.

3. **StreamSets**:
   - DataOps platform supporting CDC pipelines.

4. **Apache Kafka Connect**:
   - With plugins like Debezium, it provides a robust CDC mechanism.

5. **Oracle GoldenGate**:
   - Enterprise-grade CDC tool for Oracle databases and beyond.

---

### Common Use Cases:
1. **Data Replication**:
   - Keeping data in sync between source databases and replicas.

2. **Event Sourcing**:
   - Capturing data change events for auditing or state reconstruction.

3. **Analytics**:
   - Feeding real-time changes to analytics platforms like Apache Flink or Spark Streaming.

4. **Microservices Communication**:
   - Sharing state changes between microservices.

5. **Data Migration**:
   - Migrating data from legacy systems to modern platforms incrementally. 

CDC is a powerful technique for modern data architectures, ensuring timely and efficient data flow in distributed systems.
