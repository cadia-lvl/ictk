#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The Utils module.

This module is a collection of functions for various application for text manipulation.

ICTK: A collection of scripts to use with various Icelandic text corpora.
Copyright (C) 2020 Mál- og raddtæknistofa Gervigreindarseturs HR - Language and Voice Lab
"""
# Based on
# https://github.com/cadia-lvl/ice-asr/tree/master/ice-norm

import logging
import re

def normalize_sentence(sent, ops=list()):
	"""Normalizes a sentence.
	
	Args:
		sent: Sentance
		ops: A List of operations
		Available operations:
			- remove_punct : Removes all puctionuations from sentance.
			- remove_dash : Removes dashes preceded or followed by letters: 'Norður-Ameríka' becomes 'Norður Ameríka',
			- conform: Removes all symbols not relevant for syntax or pronunciation. 
			- remove_email : Removes any email addresss found. egs: 'user@example.com' -> ''
			- separate_acronyms : egs: 'ehf.' -> 'e h f' or 'T.d.' -> 'T d'
			- upper_to_title : Turns upper cased text to title cased, egs: 'DÓMSTÓLL' -> 'Dómstóll'
			- upper_to_lower : Turn upper cased text to title cased, egs: 'DÓMSTÓLL' -> 'dómstóll'
			- to_lower: Turn all text to lower case
			- clean_web_page_labels:  Cleans out some special web page vocabulary:
				"Þú ert hér: bb.is  Forsíða  Grein án commenta Alþjóða gjaldeyrissjóðurinn segir að tæknilega sé kreppan sé að baki." -> 
				"Alþjóða gjaldeyrissjóðurinn segir að tæknilega sé kreppan sé að baki ."
			- lemmatize : Returns the all basic form of the words 
	Returns:
		A normalized sentence from applying operations to given sentence.
	
	Example of Usage:
	normalize_sentence(
		sent='Stefndi , Jón Jónsson , er sýkn af kröfum stefnanda , Fyrirtæki ehf .',
		ops=[
			"separate_acronyms",
			"remove_punct",
			"lemmatize",
		])
	Output:
	'Stefndi Jón Jónsson er sýkn af kröfum stefnanda Fyrirtæki e h f'
	"""
	temp = sent

	for operation in ops:
		if operation ==  "clean_web_page_labels":
			temp = clean_web_page_labels(temp)
			continue
		if operation ==  "conform":
			temp = conform(temp)
			continue
		if operation ==  "lemmatize":
			temp = lemmatize(temp)
			continue
		if operation ==  "remove_dash":
			temp = remove_dash(temp)
			continue
		if operation ==  "remove_email":
			temp = remove_email(temp)
			continue
		if operation ==  "remove_punct":
			temp = remove_punct(temp)
			continue
		if operation ==  "separate_acronyms":
			temp = separate_acronyms(temp)
			continue
		if operation ==  "to_lower":
			temp = to_lower(temp)
			continue
		if operation ==  "upper_to_lower":
			temp = upper_to_lower(temp)
			continue
		if operation ==  "upper_to_title":
			temp = upper_to_title(temp)
			continue
	
	return temp


def normalize_token(token, operations=['lowercase','remove_punt']) -> Token:
	"""Returns a normalized token."""
	normalized_token = token
	return normalized_token

def remove_punct(sent):
	"""Removes all puctuation from string"""
	return sent


def remove_dash(sent):
	"""Remove_dash"""
	return sent


def conform(sent):
	"""Conform"""
	return sent


def remove_email(sent):
	"""Remove_email"""
	return sent


def separate_acronyms(sent):
	"""Separate_acronyms"""
	return sent


def upper_to_title(sent):
	"""Upper_to_title"""
	return sent


def upper_to_lower(sent):
	"""Upper_to_lower"""
	return sent


def to_lower(sent):
	"""To_lower"""
	return sent


def clean_web_page_labels(sent):
	"""Clean_web_page_labels"""
	return sent


def lemmatize(sent):
	"""Lemmatize"""
	return sent

