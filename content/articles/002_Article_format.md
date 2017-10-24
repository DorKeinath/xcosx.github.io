Title: How minimalX formats articles
Date: 2016-11-21 21:00
Tags: pelican, format
Slug: minimalx-article-format
Status: draft
Category:
HeaderImage: /images/minimalX_article_format.png
HeaderImageCaption: You can insert a caption to the header image by using the metadata element HeaderImageCaption in your .md / .rst
Summary: To make your articles stand out more, it is recommended to use header images. You can define the path to your file in the metadata element _HeaderImage_. As for the (optional) caption, you simply add the text you want to be shown in _HeaderImageCaption_. Please write tags without the hashtag, it gets added by the template. All following code snippets are examples for Markdown text files.

<!-- Credits for the background pattern of the header image: http://subtlepatterns.com -->

To make your articles stand out more, it is recommended to use header images. You can define the path to your file in the metadata element _HeaderImage_. As for the (optional) caption, you simply add the text you want to be shown in _HeaderImageCaption_. Please write tags without the hashtag, it gets added by the template. All following code snippets are examples for Markdown text files.

```
Tags: pelican, format
HeaderImage: /images/minimalX_article_format.png
HeaderImageCaption: You can insert a caption to the header image by using the metadata element HeaderImageCaption in your .md / .rst
```

This is how headlines look like:

# This is the h1 Headline
## This is the h2 Headline
### This is the h3 Headline
#### This is the h4 Headline
##### This is the h5 Headline
###### This is the h6 Headline


You can embed responsive videos from YouTube, Vimeo etc. by simply putting the untouched embed code in a div wrapper. The _adjust-width_ class optionally removes the horizontal margin on small devices to make it look nicer.


```html
<div class="videoWrapper adjust-width">
<!-- Embed code from YouTube -->
<iframe width="560" height="315" src="https://www.youtube.com/embed/d5ZOpQ5o2Ns" frameborder="0" allowfullscreen></iframe>
</div>
```


<div class="videoWrapper adjust-width">
<iframe width="560" height="315" src="https://www.youtube.com/embed/d5ZOpQ5o2Ns" frameborder="0" allowfullscreen></iframe>
</div>

The default code highlighting style is _Github_ by [pygments-css](https://github.com/richleland/pygments-css).

```javascript
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```

Pointing out selected text can be done if you set the class _content-highlight_ in the line after your text to be highlighted.

```
„Lorem ipsum dolor sit amet“
{.content-highlight}
```

You'll get some lorem ipsum now.


Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate sem et hendrerit finibus. Phasellus eget tortor ac odio varius convallis. Proin hendrerit odio ipsum, ac gravida nisi tristique eu. Ut ultricies vehicula varius. Vivamus pretium blandit placerat. Cras in tortor non dolor mattis gravida. Cras non suscipit orci. Integer sed pretium libero, sed pulvinar erat. Phasellus nec neque sit amet arcu ornare consequat vitae sed metus.


„Lorem ipsum dolor sit amet“
{.content-highlight}

Etiam malesuada ultricies malesuada. Proin hendrerit blandit nunc ut vehicula. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Etiam enim turpis, blandit in scelerisque pharetra, feugiat vel ligula. Vestibulum sit amet feugiat turpis, non cursus lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque tincidunt sapien ut dignissim semper. Duis ultricies ex at suscipit pulvinar. Aliquam erat volutpat. Sed gravida enim a sapien tempus pellentesque. Phasellus tincidunt erat sit amet blandit luctus. Fusce ullamcorper facilisis lorem cursus vestibulum.


Cras vestibulum metus non lectus mattis vehicula. Morbi pulvinar nisi at ante ullamcorper fermentum. Quisque dictum laoreet posuere. Integer elementum eu dui ac condimentum. Phasellus arcu justo, rutrum sed porttitor egestas, ultricies nec dolor. Vivamus viverra urna nec euismod pharetra. Aenean convallis ligula et magna condimentum, at efficitur neque vehicula. Vestibulum placerat hendrerit leo, at tempus tellus pretium a.

![Example image with a butterfly](/images/butterfly_example_image.jpg)
{.adjust-width}

This is an example caption
{.caption}

```
![Example image with a butterfly](/images/butterfly_example_image.jpg)
{.adjust-width}

This is an example caption
{.caption}
```

### This is an awesome list

- Item 1
- Item 2
- Item 3
- Item 4


Integer a nisi nibh. Phasellus in risus purus. Mauris vehicula euismod odio eget dictum. In cursus congue velit nec consequat. Suspendisse tempor ligula tincidunt metus tempus, sed volutpat dui feugiat. Quisque vestibulum dui vitae nunc tristique gravida. Praesent dapibus accumsan lectus, quis mollis arcu ultrices ut. Suspendisse gravida mi dapibus erat ullamcorper pellentesque. Aliquam sodales faucibus volutpat. Proin tincidunt mauris lorem, in cursus quam eleifend pellentesque.


As Kanye West said:

> We're living the future so
> the present is our past.


Integer a nisi nibh. Phasellus in risus purus. Mauris vehicula euismod odio eget dictum. In cursus congue velit nec consequat. Suspendisse tempor ligula tincidunt metus tempus, sed volutpat dui feugiat. Quisque vestibulum dui vitae nunc tristique gravida. Praesent dapibus accumsan lectus, quis mollis arcu ultrices ut. Suspendisse gravida mi dapibus erat ullamcorper pellentesque. Aliquam sodales faucibus volutpat. Proin tincidunt mauris lorem, in cursus quam eleifend pellentesque.


Github says that

>Millions of developers use GitHub to build personal projects, support their businesses, and work together on open source technologies.

I have configured my pelicanconf.py to use categories in the menu bar of the page head. If you don't configure a category in the metadata of your article, Pelican assigns the default category to it. You can set the name of the default category in your pelicanconf.py. The template is configured to not display the default category entry in the page menu since chances are low that readers are looking for uncategorized articles in a category.

```Python
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'General'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True
```
