var GenericLoader	= function(url, onComplete)
{
	// parameter polymorphism
	onComplete	= onComplete	|| function(tGeometry){};
	// define constant
	var chunkTypes	= {
		padding		: 0,
		vertexIdx	: 1,
		vertexPos	: 2,
		vertexUv	: 3,
	};
	// launch the xhr
	var xhr		= new XMLHttpRequest();
	xhr.open("GET", url, true);
	xhr.responseType= "arraybuffer"; 
	xhr.onload	= function(event){
		var arraybuffer	= xhr.response; // not responseText
		console.log('loaded', arraybuffer, arraybuffer.byteLength);

		var dataView	= new DataView(arraybuffer);
		var offset	= 0;

		console.log('dataView', dataView)
	
		while( true ){
			// skip padding
			for(; offset < dataView.byteLength && dataView.getUint8(offset) === chunkTypes.padding; offset++ );
			console.log('offset', offset)
			// detect the end of dataView
			if( offset >= dataView.byteLength )	break;
			// get chunkType
			var chunkType	= dataView.getUint8(offset);
			offset++;
			console.log(chunkType)
			if( chunkType === chunkTypes.vertexIdx ){
				var numItems		= dataView.getUint32(offset, true);
				offset			+= 4;
				var vertexIdxArray	= new Int16Array(arraybuffer, offset, numItems);
				offset			+= numItems * 2;
				// TODO handle big endian
			}else if( chunkType === chunkTypes.vertexPos ){
				var numItems		= dataView.getUint32(offset, true);
				offset			+= 4;
				var vertexPosArray	= new Float32Array(arraybuffer, offset, numItems);
				offset			+= numItems * 4;
				// TODO handle big endian
			}else if( chunkType === chunkTypes.vertexUv ){
				var numItems		= dataView.getUint32(offset, true);
				offset			+= 4;
				var vertexUvArray	= new Float32Array(arraybuffer, offset, numItems);
				offset			+= numItems * 4;
				// TODO handle big endian
			}else	console.assert(false);
		}
		console.assert(vertexIdxArray)
		console.assert(vertexPosArray)
		console.assert(vertexUvArray)
		
		// fill the attributes
		var attributes = {
			index		: {
				itemSize: 1,
				array	: vertexIdxArray,
				numItems: vertexIdxArray.length
			},
			position	: {
				itemSize: 3,
				array	: vertexPosArray,
				numItems: vertexPosArray.length
			},
			uv	: {
				itemSize: 2,
				array	: vertexUvArray,
				numItems: vertexUvArray.length
			}
		};
		var offsets	= [{
			start	: 0,
			count	: vertexIdxArray.length,
			index	: 0
		}];

		// build BufferGeometry
		var tGeometry		= new THREE.BufferGeometry();
		tGeometry.attributes	= attributes;
		tGeometry.offsets	= offsets;
		tGeometry.computeBoundingBox();
		tGeometry.computeBoundingSphere();
		tGeometry.computeVertexNormals();
		// notify the caller
		onComplete(tGeometry)
	}
	xhr.send();
}