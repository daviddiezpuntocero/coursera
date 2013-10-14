package objsets

import common._
import TweetReader._

class Tweet(val user: String, val text: String, val retweets: Int) {

  override def toString: String =
    "User: " + user + "\n" +
    "Text: " + text + " [" + retweets + "]"

}

abstract class TweetSet {

  /** This method takes a predicate and returns a subset of all the elements
   *  in the original set for which the predicate is true.
   */
  def filter(p: Tweet => Boolean): TweetSet = filter0(p, new Empty)
  def filter0(p: Tweet => Boolean, accu: TweetSet): TweetSet

  def union(that: TweetSet): TweetSet = {
    if (!this.isEmpty) this.tail.union(that.incl(this.head))
    else that
  }

  // Hint: the method "remove" on TweetSet will be very useful.
  def descendingByRetweet: TweetList = descendingByRetweet0(Nil)
  def descendingByRetweet0(accu: TweetList): TweetList

  // The following methods are provided for you, and do not have to be changed
  // -------------------------------------------------------------------------
  def incl(x: Tweet): TweetSet
  def contains(x: Tweet): Boolean
  def isEmpty: Boolean
  def head: Tweet
  def tail: TweetSet

  /** This method takes a function and applies it to every element in the set.
   */
  def foreach(f: Tweet => Unit): Unit = {
    if (!this.isEmpty) {
      f(this.head)
      this.tail.foreach(f)
    }
  }

  def remove(tw: Tweet): TweetSet

  def findMin0(curr: Tweet): Tweet =
    if (this.isEmpty) curr
    else if (this.head.retweets < curr.retweets) this.tail.findMin0(this.head)
    else this.tail.findMin0(curr)

  def findMin: Tweet =
    this.tail.findMin0(this.head)
  // -------------------------------------------------------------------------
}

class Empty extends TweetSet {

  def filter0(p: Tweet => Boolean, accu: TweetSet): TweetSet = accu
  def descendingByRetweet0(accu: TweetList): TweetList = accu

  // The following methods are provided for you, and do not have to be changed
  // -------------------------------------------------------------------------
  def contains(x: Tweet): Boolean = false
  def incl(x: Tweet): TweetSet = new NonEmpty(x, new Empty, new Empty)
  def isEmpty = true
  def head = throw new Exception("Empty.head")
  def tail = throw new Exception("Empty.tail")
  def remove(tw: Tweet): TweetSet = this
  // -------------------------------------------------------------------------
}

class NonEmpty(elem: Tweet, left: TweetSet, right: TweetSet) extends TweetSet {

  def filter0(p: Tweet => Boolean, accu: TweetSet): TweetSet = {
    if(p(elem)) left.filter0(p, right.filter0(p, accu.incl(elem)))
    else left.filter0(p, right.filter0(p, accu))
  }

  def descendingByRetweet0(accu: TweetList): TweetList = {
      val min = this.findMin
      val result = accu + min
      this.remove(min).descendingByRetweet0(result)
  }

  override def toString: String = "{" + elem + ", " + left + ", " + right + "}"

  // The following methods are provided for you, and do not have to be changed
  // -------------------------------------------------------------------------
  def contains(x: Tweet): Boolean =
    if (x.text < elem.text) left.contains(x)
    else if (elem.text < x.text) right.contains(x)
    else true

  def incl(x: Tweet): TweetSet = {
    if (x.text < elem.text) new NonEmpty(elem, left.incl(x), right)
    else if (elem.text < x.text) new NonEmpty(elem, left, right.incl(x))
    else this
  }

  def isEmpty = false
  def head = if (left.isEmpty) elem else left.head
  def tail = if (left.isEmpty) right else new NonEmpty(elem, left.tail, right)

  def remove(tw: Tweet): TweetSet =
    if (tw.text < elem.text) new NonEmpty(elem, left.remove(tw), right)
    else if (elem.text < tw.text) new NonEmpty(elem, left, right.remove(tw))
    else left.union(right)
  // -------------------------------------------------------------------------
}

trait TweetList {
  def + (tw: Tweet): TweetList
  def head: Tweet
  def tail: TweetList
  def isEmpty: Boolean
  def foreach(f: Tweet => Unit): Unit =
    if (!isEmpty) {
      f(head)
      tail.foreach(f)
    }
}

object Nil extends TweetList {
  def + (tw: Tweet): TweetList = new Cons(tw, Nil)
  def head = throw new java.util.NoSuchElementException("head of EmptyList")
  def tail = throw new java.util.NoSuchElementException("tail of EmptyList")
  def isEmpty = true
}

class Cons(val head: Tweet, val tail: TweetList) extends TweetList {
  def + (tw: Tweet): TweetList = new Cons(tw, tail + head)
  def isEmpty = false
}

object GoogleVsApple {
  val google = List("android", "Android", "galaxy", "Galaxy", "nexus", "Nexus")
  
  val apple = List("ios", "iOS", "iphone", "iPhone", "ipad", "iPad")

  val googleTweets: TweetSet = {
    TweetReader.allTweets.filter(tw => google.exists(text => tw.text.contains(text)))
  }

  val appleTweets: TweetSet = {
    TweetReader.allTweets.filter(tw => apple.exists(text => tw.text.contains(text)))
  }

  // Q: from both sets, what is the tweet with highest #retweets?
  val trending: TweetList = {
    appleTweets.union(googleTweets).descendingByRetweet
  }
}

object Main extends App {
  // Some help printing the results:
  println("RANKED:")
  GoogleVsApple.trending foreach println
}