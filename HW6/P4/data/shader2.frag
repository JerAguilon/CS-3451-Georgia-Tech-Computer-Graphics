#define PROCESSING_COLOR_SHADER

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

varying vec4 vertColor;
varying vec4 vertTexCoord;

void main() {
  gl_FragColor = vec4(1.0, vertTexCoord.t, vertTexCoord.t, 1.0);
}

