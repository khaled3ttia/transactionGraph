# TRANSactional Graph: a simple real-time order verification tool for transaction traces 

When dealing with various interleaving transactions, we need to make sure that no violation to desired properties happened. One of the crucial checks is real-time order verification. We introduce a simple tool that takes a transaction trace as input and produces a dependency graph and checks for real-time order violations.

### Prerequisites

This tool is written in Python and requires [Networkx](https://networkx.github.io/)

### Usage
To use this tool, you just need to type the following command
```
python transgraph.py path/to/trace-file
```

### Trace File Format

The repo contains a sample trace file named "trace". Please generate your traces using the same format in the included file which is for each transaction: 

```
begin_transaction-name:timestamp
write_variable-name:version-id
read_variable-name:version-id
commit_transaction-name:timestamp
```

Please note that interleaving between differnt transactions statements is not allowed (i.e, if you can't interleave statements from transactions T1 and T2)

### Output

The tool checks for cycles and violations in the graph and outputs a description of these violations(if any). Moreover, the tool saves a png image of the graph in the same working directory of the script.

