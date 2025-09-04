## Read on OLTP vs OLAP and star schemas for analytics

OLTP handles high-volume, real-time transactions, while OLAP supports complex, read-heavy analytics on aggregated and historical data; for analytics, a star schema organizes data into a central fact table linked to surrounding dimension tables to enable fast slicing and aggregation.

## Core concepts
- OLTP is optimized for many small writes with strict consistency for operational tasks like order entry and inventory updates, targeting millisecond latency and high availability for concurrent users.
- OLAP is optimized for complex reads across large, historical datasets to power reporting, trend analysis, and decision support, prioritizing query throughput over write speed.

## OLTP vs OLAP
- Purpose: OLTP runs day-to-day operations; OLAP enables analysis and planning over time.
- Workload: OLTP uses frequent INSERT/UPDATE/DELETE; OLAP uses complex SELECT with aggregations across large volumes.
- Design: OLTP databases are typically normalized to reduce redundancy; OLAP models are often denormalized (e.g., star schema) for faster reads.
- Performance: OLTP targets low-latency writes for thousands of users; OLAP targets efficient scans and aggregations, accepting higher per-query latency.
- Data freshness: OLTP holds current operational records; OLAP is periodically refreshed from OLTP sources and accumulates history.

## Star schema essentials
- A star schema has a central fact table storing measurable events (measures) and foreign keys to surrounding dimension tables that describe those events (e.g., date, product, customer, location).
- Dimension tables provide the attributes used for filtering, grouping, and slicing (e.g., product category, region, month), while fact tables hold numeric measures and keys defining dimensionality and granularity.
- Star schemas are a mature, widely adopted approach in relational data warehouses and BI tools due to simple joins and high analytical query performance.

## Fact tables
- Contain measures (e.g., sales amount, units), foreign keys to each dimension, and sometimes degenerate dimensions (e.g., order number) or surrogate keys for performance and stability.
- Dimensionality is determined by which dimensions are linked; granularity is determined by the level of detail in the keys (e.g., daily by product vs monthly by product).

## Dimension tables
- Describe entities such as products, customers, dates, and locations, typically denormalized to simplify queries and speed lookups.
- Include a primary key (often surrogate) and rich descriptive attributes that support hierarchies and user-friendly analytics.

## Why star schema for analytics
- Simplifies SQL and improves performance by minimizing joins and centralizing measures, making it ideal for BI tools and columnar warehouses.
- Encourages consistent conformed dimensions (e.g., a shared Date dimension) across subject areas and supports intuitive “slice-and-dice” analyses.

## When to choose other schemas
- Snowflake schema normalizes dimensions to reduce redundancy or manage very large, complex hierarchies, trading simpler queries for more joins.
- Galaxy (fact constellation) supports multiple related fact tables sharing conformed dimensions for broader subject coverage.

## Putting OLTP, OLAP, and star schema together
- Transactional data is captured in OLTP systems, then extracted, transformed, and loaded into an OLAP warehouse modeled as star schemas for fast analytics, reporting, and dashboards.
- This separation preserves OLTP performance and integrity while enabling scalable analytics over historical data in OLAP.[1][2]

