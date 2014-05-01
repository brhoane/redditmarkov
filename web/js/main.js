$(function () {

  $posts = $(".content .posts");
  
  $.getJSON("/data/programming.json", function (data) {
  
	for (var i = 2; i <= data.titles.length; i += 1) {
		var child = $posts.children().eq(0).clone();
		child.find(".rank").text(i);
		$posts.append(child);
	}
	renderSubreddit(data);
  })


  function renderSubreddit (subreddit) {
    $(".subreddit-name").text(subreddit.title);
    for (var ii = 0; ii <= subreddit.titles.length; ii += 1) {
      renderPost($posts.children().eq(ii), subreddit.titles[ii]);
    }
  }

  function renderPost ($post, title) {
    $post.find(".link-title").text(title);
    $post.find(".score .points").text(1000 + randInt(1000));
    $post.find(".time").text(2 + randInt(5));
    $post.find(".comment-link .count").text(5 + randInt(200));
  }

  function randInt (max) {
    return Math.floor(Math.random() * max);
  }
});
