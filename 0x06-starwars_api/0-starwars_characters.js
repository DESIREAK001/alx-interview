#!/usr/bin/node
const request = require('request');

const printCharacters = (movieId) => {
  const url = `https://swapi.dev/api/films/${movieId}`;

  request(url, { json: true }, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error(`HTTP Error: ${response.statusCode}`);
      return;
    }

    const characters = body.characters;

    characters.forEach((characterUrl) => {
      request(characterUrl, { json: true }, (err, res, charBody) => {
        if (err) {
          console.error('Error fetching character:', err);
          return;
        }

        console.log(charBody.name);
      });
    });
  });
};
