/**
  * Export compact per-file CPGs for the selected BenchmarkPython samples.
  *
  * The input file contains one CPG-relative filename per line. The output is
  * JSONL: one graph with AST, CFG, and REACHING_DEF edges per source file.
  */
@main def main(files: String, output: String): Unit = {
  import java.nio.charset.StandardCharsets
  import java.nio.file.{Files, Path, Paths}

  def json(value: String): String = {
    val builder = new StringBuilder("\"")
    value.foreach {
      case '"'  => builder.append("\\\"")
      case '\\' => builder.append("\\\\")
      case '\b' => builder.append("\\b")
      case '\f' => builder.append("\\f")
      case '\n' => builder.append("\\n")
      case '\r' => builder.append("\\r")
      case '\t' => builder.append("\\t")
      case c if c < ' ' => builder.append(f"\\u${c.toInt}%04x")
      case c => builder.append(c)
    }
    builder.append('"').toString
  }

  val selectedFiles = Files
    .readAllLines(Paths.get(files), StandardCharsets.UTF_8)
    .toArray
    .iterator
    .map(_.toString.trim)
    .filter(_.nonEmpty)
    .toVector

  val outputPath = Paths.get(output).toAbsolutePath
  Files.createDirectories(outputPath.getParent)
  val writer = Files.newBufferedWriter(outputPath, StandardCharsets.UTF_8)
  var exported = 0
  var missing = 0

  try {
    selectedFiles.foreach { file =>
      val methods = cpg.method.filenameExact(file).l
      val nodes = methods.ast.l.groupBy(_.id).valuesIterator.map(_.head).toVector.sortBy(_.id)

      if (nodes.isEmpty) {
        missing += 1
      } else {
        val nodeIds = nodes.iterator.map(_.id).toSet
        val edgeTypes = Vector("AST", "CFG", "REACHING_DEF")
        val edges = edgeTypes.flatMap { edgeType =>
          nodes.iterator
            .flatMap(node => node.outE(edgeType))
            .filter(edge => nodeIds.contains(edge.src.id) && nodeIds.contains(edge.dst.id))
            .map(edge => (edge.src.id, edge.dst.id, edgeType))
            .toVector
        }.distinct

        val nodesJson = nodes.map { node =>
          val line = node.lineNumber.map(_.toString).getOrElse("null")
          s"{\"id\":${node.id},\"label\":${json(node.label)},\"code\":${json(node.code)},\"line\":$line}"
        }.mkString(",")
        val edgesJson = edges.map { case (source, destination, edgeType) =>
          s"[$source,$destination,${json(edgeType)}]"
        }.mkString(",")

        writer.write(s"{\"sample_file\":${json(file)},\"nodes\":[$nodesJson],\"edges\":[$edgesJson]}\n")
        exported += 1
      }
    }
  } finally {
    writer.close()
  }

  println(s"Exported $exported graphs; $missing selected files had no AST nodes.")
}
