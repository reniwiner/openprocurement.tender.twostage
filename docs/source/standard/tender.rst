.. . Kicking page rebuild 2014-10-30 17:00:08
.. include:: defs.hrst

.. index:: Tender, Auction
.. _tender:

Tender
======

Schema
------

:title:
   string, multilingual, uk (title) is obligatory, en (title_en) is optional

   The name of the tender, displayed in listings. You can include the following items:

   * tender code (in procuring organization management system)
   * periodicity of the tender (annual, quarterly, etc.)
   * item being procured
   * some other info


:description:
   string, multilingual

   Detailed description of tender.

:tenderID:
   string, auto-generated, read-only

   The tender identifier to refer tender to in "paper" documentation. 

   |ocdsDescription|
   TenderID should always be the same as the OCID. It is included to make the flattened data structure more convenient.

:procurementMethodType:
    string

    value: ``aboveThresholdTS``

:procuringEntity:
   :ref:`ProcuringEntity`, required

   Organization conducting the tender.

   |ocdsDescription|
   The entity managing the procurement, which may be different from the buyer who is paying / using the items being procured.

:value:
   :ref:`value`, required

   Total available tender budget. Bids greater than ``value`` will be rejected.

   |ocdsDescription|
   The total estimated value of the procurement.

:guarantee:
    :ref:`Guarantee`

    Bid guarantee

:items:
   list of :ref:`item` objects, required

   List that contains single item being procured. 

   |ocdsDescription|
   The goods and services to be purchased, broken into line items wherever possible. Items should not be duplicated, but a quantity of 2 specified instead.

:features:
   list of :ref:`Feature` objects

   Features of tender.

:documents:
   List of :ref:`document` objects
 
   |ocdsDescription|
   All documents and attachments related to the tender.

:questions:
   List of :ref:`question` objects

   Questions to ``procuringEntity`` and answers to them.

:bids:
   List of :ref:`bid` objects

   A list of all bids placed in the tender with information about tenderers, their proposal and other qualification documentation.

   |ocdsDescription|
   A list of all the companies who entered submissions for the tender.

:minimalStep:
   :ref:`value`, required

   The minimal step of auction (reduction). Validation rules:

   * `amount` should be less than `Tender.value.amount`
   * `currency` should either be absent or match `Tender.value.currency`
   * `valueAddedTaxIncluded` should either be absent or match `Tender.value.valueAddedTaxIncluded`

:awards:
    List of :ref:`award` objects

    All qualifications (disqualifications and awards).

:contracts:
    List of :ref:`Contract` objects

:enquiryPeriod:
   :ref:`period`, required

   Period when questions are allowed.

   |ocdsDescription|
   The period during which enquiries may be made.

:tenderPeriod:
   :ref:`period`, required

   Period when bids can be submitted. At least `endDate` has to be provided.

   |ocdsDescription|
   The period when the tender is open for submissions. The end date is the closing date for tender submissions.

:qualificationPeriod:
   :ref:`period`, read-only

   This period consists of qualification and up till 5 minutes of stand still period.

   |ocdsDescription|
   Period when qualification can be submitted with stand still period.

:auctionPeriod:
   :ref:`period`, read-only

   Period when Auction is conducted.

:auctionUrl:
    url

    A web address for view auction.

:awardPeriod:
   :ref:`period`, read-only

   Awarding process period.

   |ocdsDescription|
   The date or period on which an award is anticipated to be made.

:status:
   string

   :`active.tendering`:
       Enquiries and tendering period
   :`active.pre-qualification`:
       Pre qulification period
   :`active.pre-qualification.stand-still`:
       Standstill before auction
   :`active.auction`:
       Auction period (auction)
   :`active.qualification`:
       Winner qualification (qualification)
   :`active.awarded`:
       Standstill period (standstill)
   :`complete`:
       Complete tender (complete)
   :`unsuccessful`:
       Unsuccessful tender (unsuccessful)
   :`cancelled`:
       Cancelled tender (cancelled)

   Status of the Tender.

:lots:
   List of :ref:`lot` objects.

   Contains all tender lots.

:qualifications:

   List of :ref:`Qualification` objects.

   Contains all tender qualifications.

:cancellations:
   List of :ref:`cancellation` objects.

   Contains 1 object with `active` status in case of cancelled Tender.

   The :ref:`cancellation` object describes the reason of tender cancellation contains accompanying
   documents  if any.

:revisions:
   List of :ref:`revision` objects, auto-generated

   Historical changes to Tender object properties.

.. important::

    The Tender dates should be sequential:

        * Current time
        * `enquiryPeriod.startDate`
        * `tenderPeriod.startDate`
        * `enquiryPeriod.endDate`
        * `tenderPeriod.endDate`
