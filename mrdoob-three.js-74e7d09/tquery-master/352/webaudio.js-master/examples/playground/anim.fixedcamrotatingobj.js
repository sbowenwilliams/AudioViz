console.assert( tAnim.plugins['fixedCamRotatingObj'] === undefined );
tAnim.plugins['fixedCamRotatingObj']	= {
	init	: function(){
		var world	= tQuery.world;
		world.removeCameraControls();

		tQuery('torus').position(0,1.3,0).rotation(0,0,0);		
		world.tCamera().position.set(3, 2, 5).normalize().multiplyScalar(7);;
		world.tCamera().lookAt(new THREE.Vector3(0, 1, 0));
	},
	destroy	: function(){
		
	},
	update	: function(deltaTime, present){
		var angle	= 0.2 * present * Math.PI * 2;
		var object	= tQuery('torus');
		object.rotation(0, angle, 0);
	}
};