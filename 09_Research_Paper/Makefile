# Makefile for AI-Native eBook Production preprint PDF rendering.
# Requires: pandoc, MiKTeX (xelatex), Consolas + Times New Roman + Microsoft JhengHei + Malgun Gothic fonts.
#
# Usage:
#   make           # build all PDFs into _build/
#   make en        # build only the English preprint
#   make zh        # build only the Chinese companion
#   make comments  # build only the AI evaluation panel
#   make clean     # remove _build/*.pdf
#
# Why a Makefile: locks the render command so a future maintainer (or the author
# six months from now) can reproduce the exact PDFs in the Zenodo deposit. This
# is the same reproducibility discipline the preprint itself advocates.

PANDOC := pandoc
ENGINE_OPTS := --pdf-engine=xelatex \
               --pdf-engine-opt=--enable-installer \
               --pdf-engine-opt=--interaction=nonstopmode

LAYOUT_OPTS := --include-in-header=_preamble.tex \
               --variable=geometry:margin=0.9in \
               --variable=mainfont=Times\ New\ Roman \
               --variable=monofont=Consolas \
               --variable=fontsize=11pt \
               --variable=colorlinks=true \
               --toc \
               --number-sections

BUILD := _build

EN_SRC      := 2026_AI_NATIVE_EBOOK_PRODUCTION_preprint.md
ZH_SRC      := 2026_AI_NATIVE_EBOOK_PRODUCTION_preprint_ZH.md
COMMENTS_SRC := AI_Comments_EN.md

EN_PDF       := $(BUILD)/2026_AI_NATIVE_EBOOK_PRODUCTION_preprint.pdf
ZH_PDF       := $(BUILD)/2026_AI_NATIVE_EBOOK_PRODUCTION_preprint_ZH.pdf
COMMENTS_PDF := $(BUILD)/AI_Comments_EN.pdf

.PHONY: all en zh comments clean

all: en zh comments

en: $(EN_PDF)
zh: $(ZH_PDF)
comments: $(COMMENTS_PDF)

$(EN_PDF): $(EN_SRC) _preamble.tex | $(BUILD)
	$(PANDOC) $< -o $@ $(ENGINE_OPTS) $(LAYOUT_OPTS)

$(ZH_PDF): $(ZH_SRC) _preamble.tex | $(BUILD)
	$(PANDOC) $< -o $@ $(ENGINE_OPTS) $(LAYOUT_OPTS)

$(COMMENTS_PDF): $(COMMENTS_SRC) _preamble.tex | $(BUILD)
	$(PANDOC) $< -o $@ $(ENGINE_OPTS) $(LAYOUT_OPTS)

$(BUILD):
	mkdir -p $(BUILD)

clean:
	rm -f $(BUILD)/*.pdf $(BUILD)/*.log
