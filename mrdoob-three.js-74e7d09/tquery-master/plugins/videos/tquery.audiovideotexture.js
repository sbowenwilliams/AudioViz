tQuery.registerStatic('createAudioVideoTexture', function(opts){
	return new tQuery.AudioVideoTexture(opts)
})


tQuery.registerStatic('AudioVideoTexture', function(opts){
	// handle arguments polymorphism
	if( arguments.length === 1 && typeof opts === 'string' ){
		opts	= { url : arguments[0] };
	}
	// handle default arguments
	opts	= tQuery.extend(opts, {
		world	: tQuery.world
	});
	// arguments sanity check
	console.assert( opts.url, "url MUST be specified" )

	var world	= opts.world;

	// create the video element
	var video	= document.createElement('video');
	video.width	= 320;
	video.height	= 240;
	video.autoplay	= true;
	video.loop	= true;
	video.src	= opts.url;
	this._video	= video
	this.addEventListener('destroy', function(){ video.pause()	});
	
	// create the texture
	this._tTexture	= new THREE.Texture( video );
	// hook a function to update the texture	
	var callback	= world.hook(function(){
		if( video.readyState !== video.HAVE_ENOUGH_DATA )	return;
		this._tTexture.needsUpdate	= true;
	}.bind(this));
	this.addEventListener('destroy', function(){ world.unhook(callback)	});
	
	// wait until the vid is loaded
	this._video.addEventListener('canplaythrough', function(event){
		var webaudio	= world.getWebAudio();
		// creating custom nodeChain
		var nodesChain	= WebAudio.NodeChainBuilder.create(webaudio.context())
			.mediaElementSource(this._video)
			.gainNode().analyser().panner()
		// creating the sound itself
		this._sound	= tQuery.createSound(this._world, nodesChain);
		// trigger the event
		this.dispatchEvent('soundReady')
	}.bind(this));
	this.addEventListener('destroy', function(){ this._sound.destroy()	}.bind(this));
});

tQuery.AudioVideoTexture.prototype.destroy = function(){
	this.dispatchEvent('destroy');
}

// make it eventable
tQuery.MicroeventMixin(tQuery.AudioVideoTexture.prototype)

//////////////////////////////////////////////////////////////////////////////////
//										//
//////////////////////////////////////////////////////////////////////////////////

tQuery.AudioVideoTexture.prototype.video = function() {
	return this._video;
}

tQuery.AudioVideoTexture.prototype.tTexture = function() {
	return this._tTexture;
}

tQuery.AudioVideoTexture.prototype.sound = function() {
	return this._sound;
}

