#define PROCESSING_TEXTURE_SHADER
uniform mat4 transform;
uniform mat4 texMatrix;

attribute vec4 position;
attribute vec4 color;
attribute vec3 normal;
attribute vec2 texCoord;

varying vec4 vertColor;
varying vec4 vertTexCoord;

uniform sampler2D texture;

void main() {
  vertColor = color;
  vertTexCoord = texMatrix * vec4(texCoord, 1.0, 1.0);
  vec4 currColor = texture2D(texture, vertTexCoord.xy);
  vec4 pos = position;

  float greyScale = currColor.r * .3 + currColor.g * .6 + currColor.b * .1;
  pos += vec4(normalize(normal) * greyScale * 200, 0.0);
  gl_Position = transform * pos;
}
