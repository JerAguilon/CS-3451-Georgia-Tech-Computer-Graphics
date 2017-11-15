#define PROCESSING_COLOR_SHADER

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

varying vec4 vertColor;
varying vec4 vertTexCoord;

void main() {
  gl_FragColor = vec4(0.2, 0.4, 1.0, 0.7);

  vec2 tc = mod(3.0*vertTexCoord.xy,1.0);
  if(length(vec2(0.5)-tc) < .3){
    gl_FragColor.a = 0.0;
  }
}

