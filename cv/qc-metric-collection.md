# QC metric collection
a collection of metrics, possible value and plot representations, definitions, and rationale.

I've collected QC metrics from various sources, and adapted different modes of description on which the WG will have to decide which to use for formal definition/representation and embedding in our CV. In particular I adapted the category and code scheme from the NIST metrics as it might be helpful in keeping an overview, as there are already plenty and surely more to come. Moreover, the early metrics from qcML, and discussions from PSI spring meeting in Ghent.

The more elaborate collection is found in the spreadsheet with the same name ([link](qc-metric-collection.xlsx)), a online browsable representation [here](http://htmlpreview.github.io/?https://github.com/mwalzer/qcML-development/blob/feature/QC-CV-Metric_overview/cv/qc-metric-collection.html).

**This** document is a summary with plots and definitions, as far as I had software available to calculate at least an example from a mzML file.


## Category: Filebase
* *R1-A*
	* ```File name attribute	qcML```
	* Def.: How was the MS run for this experiment labeled?
	* Ex.: "20100219_SvNa_SA_Ecoli_picked"
* R1-B
  * ```File date attribute	qcML```		
  * Def.: At what time did acquisition begin for this experiment?
  * Ex.: "2010-02-22"

## Category: Chromatography
*	C-1A
	* ```Fraction of repeat peptide IDs with	-4 min ```
	* Def.:	Estimates very early peak broadening	Fraction of all peptides identified at least 4 min earlier than max MS1 for ID
	* Ex.:	?
*	C-1B
	* ```Fraction of repeat peptide IDs with	+4 min```
	* Def.:	Estimates very early peak broadening	Fraction of all peptides identified at least 4 min earlier than max MS1 for ID
	* Ex.:	?
*	C-2A
	* ```Interquartile retention time period	Period (min)```
	* Def.:	Longer times indicate better chromatographic separation	Time period over which 50% of peptides were identified
	* Ex.:	![root](exampleplots/rt_events.png?raw=true)
*	C-2B
	* ```Interquartile retention time period	Pep ID rate```
	* Def.:	Higher rates indicate efficient sampling and identification	Rate of peptide identification during C-2A
	* Ex.:	![root](exampleplots/rt_events.png?raw=true)
*	C-3A
	* ```Peak width at half-height for IDs	Median value```
	* Def.:	Sharper peak widths indicate better chromatographic resolution	Median peak widths for all identified unique peptides (s)
	* Ex.:	TODO feature mapping
*	C-3B
	* ```Peak width at half-height for IDs	Interquartile distance```
	* Def.:	Tighter distributions indicate more peak width uniformity	Measure of the distribution of the peak widths; small values indicate consistency
	* Ex.:	TODO feature mapping
*	C-4A
	* ```Peak widths at half-max over RT deciles for IDs	First decile```
	* Def.:	Estimates peak widths at the beginning of the gradient	Median peak width for identified peptides in first RT decile (early)
	* Ex.:	TODO feature mapping
*	C-4B
	* ```Peak widths at half-max over RT deciles for IDs	Last decile```
	* Def.:	Estimates peak widths at the end of the gradient	Median peak width for identified peptides in first RT decile (end)
	* Ex.:	TODO feature mapping
*	C-4C
	* ```Peak widths at half-max over RT deciles for IDs	Median decile```
	* Def.:	Estimates peak widths at the middle of the gradient	Median peak width for identified peptides in first RT decile (middle)
	* Ex.:	TODO feature mapping
*	C-6A
	* ```Peptide elution order	max diff in first N(a, b)/10 peptides```
	* Def.:	Fraction of extra early (hydrophilic) eluters	Peptide elution order can be used to measure elution differences early (hydrophilic) and late (hydrophobic) in the chromatographic gradient.
	* Ex.:	set metric for replicates
*	C-6B
	* ```Peptide elution order	max diff in last N(a, b)/10 peptides```
	* Def.:	Fraction of extra late (hydrophobic) eluters		
	* Ex.:	set metric for replicates
*	C-7A
	* ```Interval	Acquisition range RT```
	* Def.:		What is the lowest and the highest sampled RT set to in the machine settings?
	* Ex.:	"30,3000"
*	C-7B
	* ```Interval	RT-Duration```
	* Def.:		What is the highest scan time observed minus the lowest scan time observed?
	* Ex.:	"61,2994"
*	C-8A
	* ```total ion current chromatogram	Intensity collection```
	* Def.:		the chromatogram in total (already part of mzML?)
	* Ex.:	![root](exampleplots/tic.png?raw=true)
*	C-8B
	* ```area under total ion current chromatogram	Total intensity```
	* Def.:	TIC AUC		
	* Ex.:	![root](exampleplots/auctic.png?raw=true)
*	C-8C
	* ```area under total ion current chromatogram quartiles	Intensity Q1-Q4```
	* Def.:	TIC
	* Ex.:	![root](exampleplots/auctic.png?raw=true)
*	C-8D
	* ```TIC quartile in relation to RT duration	RT-TIC Q1-Q4```
	* Def.:		The interval when the first, .., last percentile of TIC accumulates divided by RT-Duration
	* Ex.:	![root](exampleplots/rt_events.png?raw=true)
*	C-9
	* ```pump pressure chromatogram```
	* Def.:			
	* Ex.:	?
*	C-10A
	* ```MS1-TIC-Change Q2-Q4 ```
	* Def.:		The log ratio for second, .., last percentile of TIC changes over first percentile of TIC changes ? log ratio
	* Ex.:	?
*	C-10B
	* ```MS1-TIC Q2-Q4```
	* Def.:		The log ratio for second, .., last percentile of TIC over first percentile of TIC ? log ratio
	* Ex.:	![root](exampleplots/rt_events.png?raw=true)

## Category: Ion source
*	IS-1A
	* ```MS1 during middle (and early) peptide retention period	MS1 jumps >10×```
	* Def.:	Flags ESI instability	Number of times where MS1 signal greatly decreased between adjacent scans more than 10-fold (electrospray instability)
	* Ex.:	TODO RIC ? how to define early and middle RT period
*	IS-1B
	* ```MS1 during middle (and early) peptide retention period	MS1 falls >10×```
	* Def.:	Flags ESI instability	Number of times where MS1 signal greatly increased between adjacent scans more than 10-fold (electrospray instability)
	* Ex.:	TODO RIC
*	IS-2
	* ```Precursor m/z for IDs	Median```
	* Def.:	Higher median m/z can correlate with inefficient or partial ionization	Median m/z value for all identified peptides (unique ions)
	* Ex.:	![root](exampleplots/idmap.png?raw=true)
*	IS-3A
	* ```IDs by charge state (relative to 2+)	Charge 1+```
	* Def.:	High ratios of 1+/2+ peptides may indicate inefficient ionization	Number of 1+ peptides over 2+ peptides
	* Ex.:	![root](exampleplots/charge_histogram.png?raw=true)
*	IS-3B
	* ```IDs by charge state (relative to 2+)	Charge 3+```
	* Def.:	Higher ratios of 3+/2+ peptides may preferentially favor longer peptides	Number of 3+ peptides over 2+ peptides
	* Ex.:	![root](exampleplots/charge_histogram.png?raw=true)
*	IS-3C
	* ```IDs by charge state (relative to 2+)	Charge 4+```
	* Def.:	Higher ratios of 4+/2+ peptides may preferentially favor longer peptides	Number of 4+ peptides over 2+ peptides
	* Ex.:	![root](exampleplots/charge_histogram.png?raw=true)
*	IS-3D1
	* ```Charge 1 count	MS2-PrecZ-1```
	* Def.:		What fraction of MS/MS precursors is singly charged?
	* Ex.:	![root](exampleplots/charge_histogram.png?raw=true)
*	IS-3D2
	* ```Charge 2 count	MS2-PrecZ-2```
	* Def.:		What fraction of MS/MS precursors is doubly charged?
	* Ex.:	![root](exampleplots/charge_histogram.png?raw=true)
*	IS-3D3
	* ```Charge 3 count	MS2-PrecZ-3```
	* Def.:		What fraction of MS/MS precursors is triply charged?
	* Ex.:	![root](exampleplots/charge_histogram.png?raw=true)
*	IS-3D4
	* ```Charge 4 count	MS2-PrecZ-4```
	* Def.:		What fraction of MS/MS precursors is quadruply charged?
	* Ex.:	![root](exampleplots/charge_histogram.png?raw=true)
*	IS-3D5
	* ```Charge 5 count	MS2-PrecZ-5```
	* Def.:		What fraction of MS/MS precursors is quintuply charged?
	* Ex.:	![root](exampleplots/charge_histogram.png?raw=true)
*	IS-3I
	* ```?	MS2-PrecZ-likely-1```
	* Def.:		What fraction of MS/MS precursors lack known charge but look like +1s?
	* Ex.:	?
*	IS-3N
	* ```Charge n count	MS2-PrecZ-more```
	* Def.:		What fraction of MS/MS precursors is charged higher than +5?
	* Ex.:	![root](exampleplots/charge_histogram.png?raw=true)
*	IS-3X
	* ```?	MS2-PrecZ-likely-multi```
	* Def.:		What fraction of MS/MS precursors lack known charge but look like >+1s?
	* Ex.:	?


## Category: Dynamic sampling
*	DS-1A
	* ```Once/twice	Ratio```
	* Def.:	Estimates oversampling Ratio of peptides identified by 1 spectrum divided by number identified by 2 spectra		
	* Ex.:	![root](exampleplots/id_oversampling.png?raw=true)
*	DS-1B
	* ```Twice/thrice	Ratio```
	* Def.:	Estimates oversampling Ratio of peptides identified by 2 spectra divided by number identified by 3 spectra		
	* Ex.:	![root](exampleplots/id_oversampling.png?raw=true)
*	DS-2A
	* ```Spectrum counts	MS1 scans/full```
	* Def.:	Fewer MS1 scans indicates more sampling	Number of MS1 scans taken over C-2A
	* Ex.: "12091"
*	DS-2B
	* ```Spectrum counts	MS2 scans```
	* Def.:	More MS2 scans indicates more sampling	Number of MS2 scans taken over C-2A
	* Ex.: "4566"
*	DS-3A
	* ```MS1 max/MS1 sampled abundance ratio IDs	Median all IDs```
	* Def.:	Estimates position on peak where sampled for peptides of all abundances	Ratio of MS1 maximum to MS1 value at sampling for median decile of peptides by MS1 maximum intensity (1 = sampled at peak maxima)
	* Ex.:	?
*	DS-3B
	* ```MS1 max/MS1 sampled abundance ratio IDs	Med bottom 1/2```
	* Def.:	Estimates position on peak where sampled for least abundant 50% of peptides	Ratio of MS1 maximum to MS1 value at sampling for bottom 50% of peptides by MS1 maximum intensity (1 = sampled at peak maxima)
	* Ex.:	?
*	DS-4
	* ```Interval	Acquisition range m/z```
	* Def.:		What is the lowest and the highest sampled m/z set to in the machine settings?
	* Ex.:	"300,1800"
* DS-5
	* ```Top N spacing```
	* Def.: How often the top nth abundant ion was sampled in an Top N acquisition scheme
	* Ex.: ![root](exampleplots/topn.png?raw=true)

## Category: MS1
*	MS1-1
	* ```Ion injection times for IDs	MS1 median```
	* Def.:	Lower times indicate an abundance of ions	MS1 ion injection time
	* Ex.:	![root](exampleplots/injectiontimes.png?raw=true)
*	MS1-2A
	* ```MS1 during middle (and early) peptide retention period	S/N median```
	* Def.:	Higher MS1 S/N may correlate with higher signal discrimination	Median signal-to-noise value (ratio of maximum to median peak height) for MS1 spectra up to and including C-2A (needs to be clarified, also S/N = max/med vs. peak_count_normalisation(max/med))
	* Ex.:	![root](exampleplots/ms1sn.png?raw=true)
*	MS1-2B
	* ```MS1 during middle (and early) peptide retention period	TIC median```
	* Def.:	Estimates the total absolute signal for peptides (may vary significantly between instruments)	Median TIC value for identified peptides over same time period as used for MS1-2A
	* Ex.:	?
*	MS1-3A
	* ```MS1 ID max	95/5 percentile```
	* Def.:	Estimates the dynamic range of the peptide signals	Ratio of 95th over 5th percentile MS1 maximum intensity values for identified peptides (approximates dynamic range of signal)
	* Ex.:	?Features
*	MS1-3B
	* ```MS1 ID max	Median```
	* Def.:	Estimates the median MS1 signal for peptides	Median maximum MS1 value for identified peptides
	* Ex.:	?Features
*	MS1-4A
	* ```MS1 intensity variation for peptides.	Within series```
	* Def.:	Used to monitor relative intensity differences with a series	Average of between series intensity variations for identified peptides
	* Ex.:	?Features
*	MS1-4B
	* ```MS1 intensity variation for peptides.	Between/in series```
	* Def.:	Used to monitor relative intensity differences with a series compared with between series	Ratio of average intensity variation between series to average intensity variation within a series (low values indicate similarity between series)
	* Ex.:	?Features
*	MS1-5A
	* ```Precursor m/z - Peptide ion m/z	Median```
	* Def.:	Measures the accuracy of the identifications	Median real value of precursor errors
	* Ex.:	![root](exampleplots/dppm_percentile.png?raw=true)
*	MS1-5B
	* ```Precursor m/z - Peptide ion m/z	Mean absolute```
	* Def.:	Measures the accuracy of the identifications	Mean of the absolute precursor errors
	* Ex.:	![root](exampleplots/dppm_percentile.png?raw=true)
*	MS1-5C
	* ```Precursor m/z - Peptide ion m/z	ppm median```
	* Def.:	Measures the accuracy of the identifications	Median real value of precursor errors in ppm
	* Ex.:	![root](exampleplots/dppm_percentile.png?raw=true)
*	MS1-5D
	* ```Precursor m/z - Peptide ion m/z	ppm interQ```
	* Def.:	Measures the distribution of the real accuracy measurements	Interquartile distance in ppm of the precursor errors
	* Ex.:	![root](exampleplots/dppm_percentile.png?raw=true)
*	MS1-5E
	* ```Mass error observed over time```
	* Def.:	Mass error observed over retention time
	* Ex.:	![root](exampleplots/dppm_time.png?raw=true)
*	MS1-6A
	* ```number of MS events in run	MS1-Count```
	* Def.:		How many MS scans were collected?
	* Ex.:	"12091" - see DS-2A
*	MS1-7A
	* ```MS1 events in relation to RT duration	RT-MS1 Q1-Q4```
	* Def.:		The interval for the first, .., last percentile of all MS1 events divided by RT-Duration
	* Ex.:	?
*	MS1-7B
	* ```MS1 max frequency	MS1-Freq-Max```
	* Def.:		What was the fastest frequency for MS collection in any minute? (Hz)
	* Ex.:	?
*	MS1-7C
	* ```MS1 scan peak counts	MS1-Density Q1-Q4```
	* Def.:		What was the first, .., last percentile of MS scan peak counts?
	* Ex.:	?
*	MS1-8
	* ```reconstructed ion current chromatogram	Intensity collection```
	* Def.:		The reconstructed ion currents (from MS1) detected in each of a series of mass spectra recorded.
	* Ex.:	![root](exampleplots/ticric.png?raw=true)

## Category: MS2
*	MS2-1
	* ```Ion injection times for IDs	MS2 median```
	* Def.: ion injection time
	* Ex.:	![root](exampleplots/injectiontimes.png?raw=true)
*	MS2-2
	* ```MS2 ID S/N	Median```
	* Def.:	Higher S/N correlates with increased frequency of peptide identification	Median S/N (ratio of maximum to median peak height) for identified MS2 spectra
	* Ex.:	![root](exampleplots/ms2sn.png?raw=true)
*	MS2-3
	* ```MS2 ID peaks	Median```
	* Def.:	Higher peak counts can correlate with more signal	Median number of peaks in an MS2 scan
	* Ex.:	![root](exampleplots/ms2peakcount.png?raw=true)
*	MS2-4A
	* ```Fraction of MS2 identified at different MS1 max quartiles	ID fract Q1```
	* Def.:	Higher fractions of identified MS2 spectra indicate efficiency of detection and sampling	Fraction of total MS2 scans identified in the first quartile of peptides sorted by MS1 maximum intensity
	* Ex.:	![root](exampleplots/rt_events.png?raw=true)
*	MS2-4B
	* ```Fraction of MS2 identified at different MS1 max quartiles	ID fract Q2```
	* Def.:	Higher fractions of identified MS2 spectra indicate efficiency of detection and sampling	Fraction of total MS2 scans identified in the second quartile of peptides sorted by MS1 maximum intensity
	* Ex.:	![root](exampleplots/rt_events.png?raw=true)
*	MS2-4C
	* ```Fraction of MS2 identified at different MS1 max quartiles	ID fract Q3```
	* Def.:	Higher fractions of identified MS2 spectra indicate efficiency of detection and sampling	Fraction of total MS2 scans identified in the third quartile of peptides sorted by MS1 maximum intensity
	* Ex.:	![root](exampleplots/rt_events.png?raw=true)
*	MS2-4D
	* ```Fraction of MS2 identified at different MS1 max quartiles	ID fract Q4```
	* Def.:	Higher fractions of identified MS2 spectra indicate efficiency of detection and sampling	Fraction of total MS2 scans identified in the last quartile of peptides sorted by MS1 maximum intensity
	* Ex.:	![root](exampleplots/rt_events.png?raw=true)
*	MS2-5A
	* ```number of MS/MS events in run	```
	* Def.:		How many MS/MS scans were collected? - see DS-2B
	* Ex.:	"4566"
*	MS2-5B
	* ```number of MS/MS events per minute	MS2-Count```
	* Def.:			
	* Ex.:	![root](exampleplots/rt_events.png?raw=true)
*	MS2-5C
	* ```MS2 max frequency	MS2-Freq-Max```
	* Def.:		What was the fastest frequency for MS/MS collection in any minute? (Hz)
	* Ex.:	![root](exampleplots/rt_events.png?raw=true)
*	MS2-5D
	* ```MS2 scan peak counts	MS2-Density Q1-Q4```
	* Def.:		What was the first, .., last percentile of MS2 scan peak counts?
	* Ex.:	![root](exampleplots/rt_events.png?raw=true)
*	MS2-6
	* ```MS2 events in relation to RT duration	RT-MS2 Q1-Q4```
	* Def.:		The interval for the first, .., last percentile of all MS2 events divided by RT-Duration
	* Ex.:	![root](exampleplots/rt_events.png?raw=true)

## Category: Peptide identification
*	P-1
	* ```MS2 ID score	Median```
	* Def.:	Higher scores correlate with higher S/N and frequency of identification	Median peptide identification score for all peptides; higher scores generally correlate with increased MS2 S/N
	* Ex.:	Useful generalisation available?
*	P-2A
	* ```Tryptic peptide counts	Identifications```
	* Def.:	Total identifications correlate with high levels of peptide signals, performance	Number of MS2 spectra identifying tryptic peptide ions (total "spectral counts")
	* Ex.:	Useful generalisation available?
*	P-2B
	* ```Tryptic peptide counts	Ions```
	* Def.:	A good overall performance measure	Number of tryptic peptide ions identified; ions differing by charge state and/or modification state are counted separately
	* Ex.:	Useful generalisation available?
*	P-2C
	* ```Tryptic peptide counts	Peptide```
	* Def.:	A good overall performance measure	Number of unique tryptic peptide sequences identified
	* Ex.:	Useful generalisation available?
*	P-3A
	* ```Peptides Count	Semi/tryp```
	* Def.:	Indicates prevalence of semitryptic peptides in sample; increasing ratios may indicate changes in sample or in source		
	* Ex.:	Useful generalisation available?
*	P-3B
	* ```total number of missed cleavages	```
	* Def.:		The sum of the number of identifications missed cleavages
	* Ex.:	"788"
*	P-3C
	* ```enzyme contamination	```
	* Def.:	indicates the presence of a contaminant enzyme in the sample.	The ratio of the sum of chymotryptic and tryptic sequences by the number of tryptic sequences.
	* Ex.:	"1.003"
*	P-3D
	* ```Peptide lengths	```
	* Def.:	Records the length distribution of identified peptide lengths.
	* Ex.:	![root](exampleplots/lengthdistro.png?raw=true)
*	P-4A
	* ```number of PSM count```
	* Def.:			
	* Ex.: "20078"
*	P-4B
	* ```number of peptides	Peptides count```
	* Def.:			
	* Ex.:	"9013"
*	P-5A
	* ```average number of PSMs per inferred protein	mean count```
	* Def.:			
	* Ex.:	?
*	P-5B
	* ```number of proteins	Protein count```
	* Def.:			
	* Ex.:	"6005"
*	P-5C
	* ```number of uniquely identified proteins	uniquely id protein count```
	* Def.:	The number of proteins identified by peptide matching just this protein.
	* Ex.:	"78"
*	P-6
	* ```Mass error histogram	deltaM Q1-Q4```
	* Def.:		Q1 depends on search engine tolerance setting, Q2 should be 0 ideally.
	* Ex.:	![root](exampleplots/dppm_percentile.png?raw=true)
*	P-7A
	* ```Reference comparison number of Identifications	Within series```
	* Def.:		could be calculated for applicable reference run or many spike-in proteins and many theo. ratios, e.g. diff_theo_vs_meas_ratio_of_spike_in_BSA_2.5
	* Ex.:	?
*	P-7B
	* ```Reference comparison Mean Intensities```
	* Def.:		could be calculated for applicable reference run or many spike-in proteins and many theo. ratios, e.g. diff_theo_vs_meas_ratio_of_spike_in_BSA_2.5
	* Ex.:	?
*	P-8A
	* ```id ratio```
	* Def.:		This ratio indicates the number of identified peptides vs. the number of recorded ms2 spectra.
	* Ex.:	![root](exampleplots/idmap.png?raw=true)
*	P-8B
	* ```id coverage```
	* Def.:		The coverages of distinct sequences for a respective engine.
	* Ex.:	?
* P-9
	* ```Hydropathy index of identified peptides over retention time ```
	* Def.: Hydropathy index of identified peptides over retention time
	* Ex.:  ![root](exampleplots/gravy.png?raw=true)
* P-10
 	* ```Fractional mass plot```
 	* Def.: The neutral mass [M] of identified peptides plotted by fractional over nominal mass against the theoretically possible peptides by the given database or organism
 	* Ex.: ![root](exampleplots/fracmass.png?raw=true)

## Category: Feature Extraction
*	F-1A
	* ```number of features	Feature count```
	* Def.:		Number of features detected
	* Ex.:	"10308"
*	F-1B
	* ```number of identified features	Feature count```
	* Def.:		Number of detected features with attached identifications.
	* Ex.:	"5567"
	* ![root](exampleplots/mapped_features.png?raw=true)
*	F-1C
	* ```Features observed over time```
	* Def.:		Number of detected features over the retention time interval.
	* Ex.:	![root](exampleplots/feat_time.png?raw=true)
*	F-2A
	* ```FWHM of observed features```
	* Def.:		The full width at half maximum values of the observed features
	* Ex.:	![root](exampleplots/feat_width.png?raw=true)
*	F-2B
	* ```Fraction of precursors generating top and bottom half peak width	XIC-WideFrac```
	* Def.:		What fraction of precursor ions account for the top half of all peak width?
	* Ex.:	?
*	F-2C
	* ```FWHM Quartiles	XIC-FWHM Q1-Q4```
	* Def.:		What is the first, .., last percentile of peak widths for the wide XICs?
	* Ex.:	![root](exampleplots/feat_width.png?raw=true)
*	F-2D
	* ```Feature height quartiles 2-4 (in relation to Q1)	XIC-Height Q2-Q4```
	* Def.:		The log ratio for first, .., third percentile of wide XIC heights over first percentile of heights.
	* Ex.:	?
