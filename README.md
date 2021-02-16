Django webapp for Kindle highlights.

Context: KindlerWeb is a product I tried to build in early 2020. Lets you build a garden around your Kindle highlights. Friends walk around and join in- ruminate on your highlights, ask you why you found something interesting, hoard highlights they like etc. I'll get back to building this once my UI/UX skills are better.

I host an incomplete demo at https://kindlerweb.herokuapp.com/.

OpenKindlerWeb lets you deploy your own instance of KindlerWeb on Heroku. You can easlily set up your instance by pasting a secret key in `settings.py`. I will soon write detailed instructions on how you can do that.
 
This project was inspired by Sawyer H's [Reading Highlights](https://highlights.sawyerh.com/) page. Another inspiration is the excellent [Readwise.io] (https://readwise.io/) app.

The larger plan is to implement a [spaced repetition system](https://en.wikipedia.org/wiki/Spaced_repetition) back-end, something like the excellent Readwise.io webapp, once the "highlight garden" side of the product is implemented to fruition. The MVP will let you generate Anki decks.

If this interests you, I'd love to chat. I'm @sanjaymaniam everywhere. In the meantime, contributions and suggestions are always welcome.

Thanks to the amazing [@TheInkEdge](https://www.instagram.com/theinkedge/?hl=en) for help with the front-end!

- To Do:
  - [ ] Write a "How To Set Your KindlerWeb Up" section
  - [ ] Brainstorm: How do you let people join in and ruminate on ideas they find interesting?
