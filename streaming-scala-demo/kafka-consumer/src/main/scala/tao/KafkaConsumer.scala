package tao

import akka.actor.ActorSystem
import akka.kafka.scaladsl.Consumer
import akka.kafka.{ConsumerSettings, Subscriptions}
import akka.stream.scaladsl.Sink
import akka.stream.{ActorMaterializer, Materializer}
import akka.util.ccompat.JavaConverters
import io.confluent.kafka.serializers.{AbstractKafkaAvroSerDeConfig, KafkaAvroDeserializer, KafkaAvroDeserializerConfig}
import org.apache.avro.specific.SpecificRecord
import org.apache.kafka.common.serialization.{Deserializer, StringDeserializer}

object KafkaConsumer {
  def main(args: Array[String]): Unit = {
    implicit val actorSystem: ActorSystem = ActorSystem()
    implicit val actorMaterializer: Materializer = ActorMaterializer()

    val config = actorSystem.settings.config.getConfig("akka.kafka.consumer")

    val kafkaAvroSerDeConfig = Map[String, Any] (
      AbstractKafkaAvroSerDeConfig.SCHEMA_REGISTRY_URL_CONFIG -> "http://localhost:8081",
      KafkaAvroDeserializerConfig.SPECIFIC_AVRO_READER_CONFIG -> true.toString
    )

    val consumerSettings: ConsumerSettings[String, SpecificRecord] = {
      val kafkaAvroDeserializer = new KafkaAvroDeserializer()
      kafkaAvroDeserializer.configure(JavaConverters.mapAsJavaMap(kafkaAvroSerDeConfig), false)
      val deserializer = kafkaAvroDeserializer.asInstanceOf[Deserializer[SpecificRecord]]

      ConsumerSettings(actorSystem, new StringDeserializer, deserializer)
    }

    val done = Consumer
        .plainSource(consumerSettings, Subscriptions.topics("test"))
      //.plainSource(kafkaConsumerSettings, Subscriptions.topics("test"))
      //.asSourceWithContext(_.committableOffset)
      .map(_.value())
      .log("received message")
      //.run()
      //.log("value is:", _.value())
      //.mapConcat(_.value().split(",").toIterator)
      //.map()
      //.map(_.value())
      //.log("value is:", _.toString)
      //.mapConcat(x=> x.value().split(","))
      //.flatMapConcat(_.split(","))
      .runWith(Sink.foreach(println)) // just print each message for debugging

/*    implicit val ec: ExecutionContextExecutor = actorSystem.dispatcher
    done onComplete  {
      case Success(_) => println("Done"); actorSystem.terminate()
      case Failure(err) => println(err.toString); actorSystem.terminate()
    }*/
  }

}
