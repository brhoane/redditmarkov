$(function () {
  if (window.location.pathname == "/list.html") { return; }

  var $posts = $(".content .posts");
  var params = getSearchParameters();
  var subreddit = params.subreddit || "programming";

  $.getJSON("/data/" + subreddit + ".json", function (data) {
    for (var i = 2; i <= data.titles.length; i += 1) {
      var child = $posts.children().eq(0).clone();
      child.find(".rank").text(i);
      $posts.append(child);
    }

    renderSubreddit(data);
  });


  function renderSubreddit (subreddit) {
    var maxPosts = subreddit.titles.length > 25 ? 25 : subreddit.titles.length;

    $(".subreddit-name").text(subreddit.title);

    for (var ii = 0; ii <= maxPosts; ii += 1) {
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

  /* Code to get query parameters from the url copied from:
   * http://stackoverflow.com/questions/5448545/how-to-retrieve-get-parameters-from-javascript
   */
  function getSearchParameters() {
    var prmstr = window.location.search.substr(1);
    return prmstr != null && prmstr != "" ? transformToAssocArray(prmstr) : {};
  }

  function transformToAssocArray(prmstr) {
    var params = {};
    var prmarr = prmstr.split("&");
    for (var i = 0; i < prmarr.length; i++) {
      var tmparr = prmarr[i].split("=");
      params[tmparr[0]] = tmparr[1];
    }
    return params;
  }
});
