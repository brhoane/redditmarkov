$(function () {
  var data = {
    subreddits: [
      {
        title: "all",
        url: "all",
        titles: [
          "unfortunately i am molly ringwald ama",
          "whale",
          "correct me if i’m a person",
          "my [ff]riend and i invented ethernet - ama",
          "the progression of a roomba outfitted with leds",
          "my friend sent me this",
          "rare lynx sighting in colorado tomorrow",
          "wanted to get back into painting so i took a picture of my favorite christmas present this year",
          "this makes me laugh",
          "saw this old electric coffee table"
        ]
      }
    ]
  },
  $posts = $(".content .posts");

  for (var i = 2; i < 11; i += 1) {
    var child = $posts.children().eq(0).clone();
    child.find(".rank").text(i);
    $posts.append(child);
  }

  renderSubreddit(data.subreddits[0]);

  function renderSubreddit (subreddit) {
    $(".subreddit-name").text(subreddit.title);
    for (var ii = 1; ii <= 10; ii += 1) {
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
