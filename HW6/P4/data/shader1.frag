#define PROCESSING_TEXTURE_SHADER

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

uniform sampler2D texture;

varying vec4 vertColor;
varying vec4 vertTexCoord;

void main() { 
  vec4 currPix = texture2D(texture, vertTexCoord.xy);
  float currGrey = (currPix.r)*0.3+(currPix.g)*0.6+(currPix.b)*0.1;

  vec4 left = texture2D(texture, vec2(vertTexCoord.x-.01,vertTexCoord.y).xy);
  vec4 up = texture2D(texture, vec2(vertTexCoord.x,vertTexCoord.y+.01).xy);
  vec4 right = texture2D(texture, vec2(vertTexCoord.x+.01,vertTexCoord.y).xy);
  vec4 down = texture2D(texture, vec2(vertTexCoord.x,vertTexCoord.y-.01).xy);
  
  float leftGrey = left.r*0.3+left.g*0.6+left.b*0.1;
  float rightGrey = right.r*0.3+right.g*0.6+right.b*0.1;
  float upGrey = up.r*0.3+up.g*0.6+up.b*0.1;
  float downGrey = down.r*0.3+down.g*0.6+down.b*0.1;

  float e = (leftGrey+upGrey+rightGrey+downGrey)-(4*currGrey);
  vec4 edgeColor = vec4(e,e,e,1);
  gl_FragColor = vec4(edgeColor.rgb*4, 1.0);
}
