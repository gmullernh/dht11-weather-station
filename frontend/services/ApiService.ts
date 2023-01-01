import { IData } from '~/models/DataModel'

export async function getDataFromAPI(): Promise<IData> {
  try {

    // assumes that you're running the API on the same machine
    var origin = window.location.origin;  
    var port = 81 // the default port for the API

    const result = await fetch(`${origin}:${port}/api/v2/json`, { method: 'GET' });
    const json = await result.json();
    
    return {
      date: json.datetime,
      humidity: parseInt(json.humidity),
      temperature: parseInt(json.temperature)
    };

  } catch (error) {
    throw new Error('Error recovering content: ' + error)
  }
}