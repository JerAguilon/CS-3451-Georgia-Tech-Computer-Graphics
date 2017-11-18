#define PROCESSING_COLOR_SHADER

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

varying vec4 vertColor;
varying vec4 vertTexCoord;

void main() {
	

  gl_FragColor;

  float r = 0.0;
  float i = 0.0;

  float x = vertTexCoord.x*3.0 - 2.1; // [2.1,.9]
  float y = vertTexCoord.y*3.0 - 1.5; // [-1.5,1.5]

  bool red = false;

  for (int count =0; count < 20; count++) {
  	float currR = r*r - i*i;
  	float currI = 2 * r * i;
  	r = currR + x;
  	i = currI + y;
  	if (sqrt(r * r + i * i) > 2) {
  		red = true;
  		break;
  	}
  }

  if (red) {
  	gl_FragColor = vec4(1.0,0.0,0.0,1.0);
  } else {
  	gl_FragColor = vec4(1.0,1.0,1.0,1.0);
  }
}

