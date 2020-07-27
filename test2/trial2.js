async function Pokeget(id){
  console.log(id);
  const url = "https://pokeapi.co/api/v2/pokemon/${id}";
  const res = await fetch(url);
  const pokemon = await res.json();
  console.log(pokemon.name);
}

Pokeget(1);
