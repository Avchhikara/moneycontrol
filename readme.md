# MoneyControl scrapper

This package basically scrape the moneycontrol.com website.

### Installation

`pip install moneycontrol`

### Functionalities supported for now

1. **Getting an article**

   Usage:

   ```
   from moneycontrol.ArticleExtractor import get_article
   article = get_article(article_url)
   ```

   Article object would look like:

   ```
   {
       'title': 'Despite...',
       'summary': 'Many investors ...',
       'timestamp': '2021-04-02 11:34:00',
       'author': 'Dev Ashish',
       'img_url': 'https://images.moneycontrol.com/...,
       'content': 'Before we discuss that, let us quickly see how PPF interest is calculated. This assumes significance as many people invest Rs 1.5 lakh in PPF ... ',
       'tags': [
           'Fixed Income',
           'personal finance',
           'PPF',
           'Small Savings Scheme',
           '...'
       ]
   }
   ```

### May support in future

1. **Getting company financial data (moneycontrol has a lot of it)**
1. anything else

## Did it help?

You can be my motivation 😀

Support me here:

_by scanning the following the QR code in any UPI payment supported app_

![](https://res.cloudinary.com/mrmagician/image/upload/c_scale,h_117,q_100/v1617404364/qr-code_fpsmvi.png)

**or**

_by using the following upi-id_: **mr.magician@ybl**
