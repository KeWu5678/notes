

a prompt containing the setting, constraints, targets are fed to the agents. 
There is a orchestrator to consult (the main interface, claude code). It understands and decompose the task and assign the task to different work


# ROLES
## Orchestrator
main-agent
stdin: fact_graph + global memory
skill: [elaboration/SKILL.md](file:///Users/chaoruiz/Documents/Repos/math-agent/Danus/.claude/skills/elaboration/SKILL.md)
stdout: 

## Consult
Core idea: **stateless**. 
1. The elabration is the whole prompt; no previous history is prompt. 
2. A temporary directory; no Claude.md or other system level file is read. 
The core implementation scaffold is the CLI, which remove the in-memory session between the call and create the stdio. 

## Worker


## Verify
Core idea: **statelessness** and **affordance**. Explain why we use MCP instead of the CLI in this case. 


## Writting
Core idea: **affordance**. 
Use the MCP to declare what the external system allows the agent to do, along with the
- standardized contract
- tools
- resources



# ARCHITECTURE
Layer
1. the main agent: interaction with the user. Keep tracking and the adminitrative
- created at the start; updated in each consult call. 
- it records the progress and the decision. 

## Database
1. fact graph
- Created the DAG with the datatype FACT. 

2. global memory
The global memory is the structured json file. Every memory is dic with kind and status. 
- "master_guidance", 
- 

3. local memories
- local memory

## CLI vs MCP
1. The essence of MCP lies in the standarized interface contract: 
- what are the tools
- how the schema is declared
- how to use and call
```
  {
    "name": "read_file",
    "description": "Read a file's contents",
    "inputSchema": {
      "type": "object",
      "properties": { "path": { "type": "string" } },
      "required": ["path"]
    }
  }
```

2. MCP basically defines a microservice. It make things determinstic, which solve some problems caused by the probalistic nature of the LLM. 





- logs

## CLI

## Tools

## Skills
each skill has 
1. input-output contract
2. procedure
3. available tools
4. failure mode


# PRINCIPLE

- brain in a vat
- reward hacking
- self-correction
- statelessness

## statelessness

## role separation
1. context-leaking





# IMPROVEMENT: 
1. structured output & tool bind
2. can we use langfuse to increase the observability 
 