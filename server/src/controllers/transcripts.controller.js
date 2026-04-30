import { parseHTML } from 'linkedom';
import { Defuddle } from 'defuddle/node';

export const getTranscript = async (req, res) => {
  const { url } = req.query;

  try {
    const response = await fetch(url);
    const htmlString = await response.text();

    const { document } = parseHTML(htmlString);
    const result = await Defuddle(document, url, { markdown: true });

    res.setHeader('Content-Type', 'text/plain');
    res.send(result.content);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};