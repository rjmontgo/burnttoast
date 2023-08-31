# Burnt Toast Project 


## Motivation

I have done a lot of JSON API engineering my career, and this seemed a good change of pace. It has a lot of things
I like:

- Video Games
- Python

And a lot of things I want to learn more about:

- Three.js
- 3D Modeling
- client/server state reconciliation over a websocket

## Dev Setup

<details open>
<summary> Nix (Recommended) </summary>
  1. Install [Nix](https://nixos.org/download)
  2. [Optional] Install [Direnv]()
     This enables nix to load your environment in your preferred shell every time you switch into it.

     Once installed, allow direnv to use the flake directory with `direnv allow .`
  
  3. Finally, run

    `nix develop`
  
    This will install all needed project dependencies and drop you in a shell with those dependencies loaded 
    into your path.

</details>


## FAQ

- **Why did you use nix? What is nix?**
  
  [Nix](https://nixos.org/) is a functional DSL for specifying reproducible builds and deployments. As to why, because
  it simplifies my setup (even if it does look a little weird), and grants me a higher granularity of 
  control over my installed packages. 
  
  It also means that if anyone wants to run this on their own machine I don't have to worry as much
  about any dependency resolution issues they may have. Unfortunately, while Python is a great language
  it has some packaging issues, [relevant XKCD](https://xkcd.com/1987/). It's not the only language with 
  this type of problem (👀 Javascript & NPM). 
  
  I __might__ add virtualenv support in the future, sense it seems like the most sensible option, but
  I'm happy with nix for now.


- **Why did you choose Python?** 
  
  Because it's easy to work with, has tons of library support, and is a language 
  I'm comfortable with. 

### Works Cited

- [Gabriel Gambetta / Client Server Game Architecture](https://www.gabrielgambetta.com/client-server-game-architecture.html)
