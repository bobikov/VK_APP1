$(document).ready(function(){
	$(".login_button").click(function(){VK.Auth.login(authInfo);});
	  VK.init({
	    apiId: 4964195

	  });

function authInfo(response) {
	  if (response.session) {
	    $(".status1").text('user: '+response.session.mid + " now is logged");
	  } else {
	    alert('not auth');
	  }
	}
VK.Auth.getLoginStatus(authInfo);

// Click button events

	$(".getperm").click(function(){
			getAccPerm("179349317");
	});
	$(".post").click(function(){
			postToVk("Hello");

	});
	$(".getph").click(function(){
			var uaid = $("#uaid").val();
			// GetPhotos("-44426090");
		
			$(".status3").html('');
			GetPhotos(uaid);
	});

// Wall post
	function postToVk(msg){ 
			VK.Api.call( 'wall.post',
			{
				owner_id: '179349317',
				message: msg
			},
				function(response) {
				console.log(response);
				}
			);

	}
//Get Permissions
	function getAccPerm(id){
			VK.Api.call("account.getAppPermissions, ", {
				user_id: id
			},
				function(data){
				console.log(data.response);
				}
			);
	}
//Get Albums
	function GetPhotos(id){
		VK.Api.call("photos.getAlbums", {
			owner_id: id
		}, 
			function(data){
			if(data.response){
				var obj = data.response;
			

					// $(".status3").html(
					// '<table border="1" cellspacing="0" cellpadding="10">'+
					// '<tr><td>album_id:</td><td>' + obj.aid+ "</td></tr>" + 
					// '<tr><td>owner_id:</td><td> ' + obj.owner_id+ "</td></tr>" + 
					// '<tr><td>title:</td><td> ' + obj.title+ "</td></tr>" +
					// '<tr><td>thumb_id:</td><td> ' + obj.thumb_id+ "</td></tr>"+
					// '<tr><td>size:</td><td> ' + obj.size+ "</td></tr>"+
					// "</table>"
					// );
				// $("<div>"+key + element.owner_id+"</div>").appendTo($(".status3"));
				$.each(obj, function(key, element){
					$("<table style='float:left' border='1' cellpadding='6' cellspacing='0'><tr><td>Title</td><td>"+element.title+"<tr><td>AlbumID</td><td>" + element.aid + "</td></tr><tr><td>Size</td><td>" + element.size + "</td></tr></table>").appendTo($(".status3"));
				});
					console.log(data.response);
			}
			else {
					console.log(data);
			}
			});
	}


// Get list of photos
// 
// 
// 

$("h1").click(function(){
	$(this).next().toggle();
});
});