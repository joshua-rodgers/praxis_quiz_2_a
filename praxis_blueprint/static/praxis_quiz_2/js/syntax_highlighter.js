const keywordPatterns = [
  /\bprocedure\b/g,
  /\bend procedure\b/g,
  /\bif\b/g,
  /\bend if\b/g,
  /\brepeat\b/g,
  /\buntil\b/g,
  /\bfor\b/g,
  /\bend for\b/g,
  /\bwhile\b/g,
  /\bend while\b/g,
  /\breturn\b/g,
];

const typePatterns = [/\bint\b/g, /\bboolean\b/g, /\bString\b/g, /\bdouble\b/g, /\bvoid\b/g];

const operatorPatterns = [/←/g, /≠/g, /≤/g, /≥/g];

function applyHighlighting(element) {
  let html = element.textContent;

  html = html.replace(/\/\*[\s\S]*?\*\//g, (match) => `__COMMENT__${match}__ENDCOMMENT__`);
  html = html.replace(/\/\/.*$/gm, (match) => `__COMMENT__${match}__ENDCOMMENT__`);

  html = html.replace(/"([^"\\]|\\.)*"/g, (match) => `__STRING__${match}__ENDSTRING__`);
  html = html.replace(/\b\d+(\.\d+)?\b/g, (match) => `__NUMBER__${match}__ENDNUMBER__`);

  operatorPatterns.forEach((pattern) => {
    html = html.replace(pattern, (match) => `__OPERATOR__${match}__ENDOPERATOR__`);
  });

  keywordPatterns.forEach((pattern) => {
    html = html.replace(pattern, (match) => `__KEYWORD__${match}__ENDKEYWORD__`);
  });

  typePatterns.forEach((pattern) => {
    html = html.replace(pattern, (match) => `__TYPE__${match}__ENDTYPE__`);
  });

  html = html
    .replace(/__COMMENT__([\s\S]*?)__ENDCOMMENT__/g, '<span class="token comment">$1</span>')
    .replace(/__STRING__(.*?)__ENDSTRING__/g, '<span class="token string">$1</span>')
    .replace(/__NUMBER__(.*?)__ENDNUMBER__/g, '<span class="token number">$1</span>')
    .replace(/__OPERATOR__(.*?)__ENDOPERATOR__/g, '<span class="token operator">$1</span>')
    .replace(/__KEYWORD__(.*?)__ENDKEYWORD__/g, '<span class="token keyword">$1</span>')
    .replace(/__TYPE__(.*?)__ENDTYPE__/g, '<span class="token type">$1</span>');

  element.innerHTML = html;
}

window.PraxisSyntaxHighlighter = {
  applyHighlighting,
};

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".praxis-code-block").forEach((block) => {
    applyHighlighting(block);
  });
});
