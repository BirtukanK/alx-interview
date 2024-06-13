#!/usr/bin/node

const axios = require('axios');

async function fetchCharacters (movieId) {
  const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';

  try {
    const movieResponse = await axios.get(`${baseUrl}${movieId}/`);
    const movieData = movieResponse.data;

    const characterUrls = movieData.characters;

    for (const url of characterUrls) {
      const charResponse = await axios.get(url);
      const charData = charResponse.data;
      console.log(charData.name);
    }
  } catch (error) {
    console.error(`Error fetching data: ${error}`);
  }
}

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: node script.js <Movie ID>');
  process.exit(1);
}

fetchCharacters(movieId);
