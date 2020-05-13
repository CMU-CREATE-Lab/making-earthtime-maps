function hexToRgb(hex) {
  // Expand shorthand form (e.g. "03F") to full form (e.g. "0033FF")
  var shorthandRegex = /^#?([a-f\d])([a-f\d])([a-f\d])$/i;
  hex = hex.replace(shorthandRegex, function(m, r, g, b) {
    return r + r + g + g + b + b;
  });

  var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
  return result ? {
    r: parseInt(result[1], 16),
    g: parseInt(result[2], 16),
    b: parseInt(result[3], 16)
  } : null;
}

function rgbToHex(r, g, b) {
  return "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
}

function hexToRgbNormalized(hex) {
  var inputHex = document.getElementById("hex2-input").value || hex;
  var c = hexToRgb(inputHex);
  var cNormalized = "[" + parseFloat(c.r / 255.0).toFixed(4) + ", " + parseFloat(c.g / 255.0).toFixed(4) + ", " + parseFloat(c.b / 255.0).toFixed(4) + ", 1]";
  var normalizedColorDomField = document.getElementById("normalizedColor");
  if (normalizedColorDomField) {
    normalizedColorDomField.innerHTML = cNormalized;
  } else {
    return cNormalized;
  }
}

function hexToPackedColor(hex) {
  var inputHex = document.getElementById("hex-input").value || hex;
  var c = hexToRgb(inputHex);
  var packedColor = parseFloat(c.r + c.g * 256 + c.b * 256.0 * 256.0).toFixed(1);
  var packedColorDomField = document.getElementById("packedColor");
  if (packedColorDomField) {
    packedColorDomField.innerHTML = packedColor;
  } else {
    return packedColor;
  }
}
