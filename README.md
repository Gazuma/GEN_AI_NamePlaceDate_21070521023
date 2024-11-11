<h1>Tagging Name, Place, Date using Python</h1>
<h6>Name - Deep Raut PRN - 21070521023 Section - A Sem - 7</h6>
<p>This project demonstrates how to extract names, places, and dates from a text file using <code>spacy</code> for NLP processing and regular expressions for date detection.</p>

<h2>Requirements</h2>
<ul>
  <li>Python 3</li>
  <li><code>spacy</code> library</li>
  <li>Pre-trained model: <code>en_core_web_sm</code> for POS tagging</li>
  <li>A JSON file named <code>cities2.json</code> containing city names</li>
</ul>

<h2>Code Description</h2>

<p>The main tasks performed in this code are:</p>
<ul>
  <li>Loading <code>spacy</code>'s English model for part-of-speech (POS) tagging.</li>
  <li>Using regular expressions to detect common date formats in the text.</li>
  <li>Loading a JSON file (<code>cities2.json</code>) with a collection of city names to identify known places.</li>
</ul>

<h3>Functions</h3>
<ul>
  <li><code>extract_entities(file_path)</code>: Takes the path of a text file as input and extracts:
    <ul>
      <li><strong>Names</strong>: Extracted using POS tagging for proper nouns.</li>
      <li><strong>Dates</strong>: Detected using a regex pattern to match multiple date formats.</li>
      <li><strong>Places</strong>: Identified by matching words in the text against the loaded city names.</li>
    </ul>
  </li>
</ul>

<h2>Usage</h2>
<ol>
  <li>Load required libraries by running <code>pip install spacy</code> and downloading the English model with <code>python -m spacy download en_core_web_sm</code>.</li>
  <li>Ensure <code>file.txt</code> (input text) and <code>cities2.json</code> (city data in JSON format) are in the same directory as the script.</li>
  <li>Run the script to extract entities:
    <pre><code>python script.py</code></pre>
  </li>
</ol>

<h2>Example Output</h2>
<p>After running the script, it will print the extracted information:</p>
<pre><code>
Names: ['Alice', 'London']
Places: ['London']
Dates: ['Jan 15, 2023']
</code></pre>
