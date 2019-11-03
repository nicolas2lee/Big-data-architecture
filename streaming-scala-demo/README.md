# Akka stream with kafka

## source

### plain source
#### plain source
use case:
* offset is stored externally (can realize exactly once semantics when the result and offset in the same transaction)
* auto-commit (default disabled)


    The `plainSource` emits `ConsumerRecord` elements (as received from the underlying `KafkaConsumer`).
    It has no support for committing offsets to Kafka. It can be used when the offset is stored externally
    or with auto-commit (note that auto-commit is by default disabled).
   
    The consumer application doesn't need to use Kafka's built-in offset storage and can store offsets in a store of its own
    choosing. The primary use case for this is allowing the application to store both the offset and the results of the
    consumption in the same system in a way that both the results and offsets are stored atomically. This is not always
    possible, but when it is, it will make the consumption fully atomic and give "exactly once" semantics that are
    stronger than the "at-least once" semantics you get with Kafka's offset commit functionality.

#### plainPartitionedSource
#### plainPartitionedManualOffsetSource
#### plainExternalSource

### committable source
#### committableSource
use case:
The offset will be committed to kafka. If you want to store offset externally, should use plain source
Difference between committable source and auto commit:
* committable source can customize whether a message is consumed or not 
* auto commit is configurable for commit interval


    The `committableSource` makes it possible to commit offset positions to Kafka.
    This is useful when "at-least once delivery" is desired, as each message will likely be
    delivered one time but in failure cases could be duplicated.
   
    If you commit the offset before processing the message you get "at-most once delivery" semantics,
    and for that there is a [[#atMostOnceSource]].
   
    Compared to auto-commit, this gives exact control over when a message is considered consumed.
   
    If you need to store offsets in anything other than Kafka, [[#plainSource]] should be used
    instead of this API.
#### commitWithMetadataSource
nearly same as committable source, besides adding meta data
   
    The `commitWithMetadataSource` makes it possible to add additional metadata (in the form of a string)
    when an offset is committed based on the record. This can be useful (for example) to store information about which
    node made the commit, what time the commit was made, the timestamp of the record etc.
#### committablePartitionedSource
#### commitWithMetadataPartitionedSource
#### committableExternalSource

### atMostOnceSource
use case: at-most once
commit offset to kafka before consuming message

    Convenience for "at-most once delivery" semantics. The offset of each message is committed to Kafka
    before it is emitted downstream.

## producer 
## consumer

### drainAndShutdown
Terminate all process for all received messaging, and close the source (so no more message could be consumed), once treatment of all messages terminated, app close

https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-aws-cli 