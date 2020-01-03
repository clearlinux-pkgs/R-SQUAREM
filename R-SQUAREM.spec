#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-SQUAREM
Version  : 2017.10.1
Release  : 24
URL      : https://cran.r-project.org/src/contrib/SQUAREM_2017.10-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/SQUAREM_2017.10-1.tar.gz
Summary  : Squared Extrapolation Methods for Accelerating EM-Like Monotone
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : R-setRNG
BuildRequires : buildreq-R

%description
monotone sequences from smooth, contraction mapping such as the
        EM algorithm. It can be used to accelerate any smooth, linearly
        convergent acceleration scheme.  A tutorial style introduction
        to this package is available in a vignette on the CRAN download
        page or, when the package is loaded in an R session, with
        vignette("SQUAREM").

%prep
%setup -q -c -n SQUAREM

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552952705

%install
export SOURCE_DATE_EPOCH=1552952705
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library SQUAREM
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library SQUAREM
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library SQUAREM
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  SQUAREM || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/SQUAREM/DESCRIPTION
/usr/lib64/R/library/SQUAREM/INDEX
/usr/lib64/R/library/SQUAREM/Meta/Rd.rds
/usr/lib64/R/library/SQUAREM/Meta/demo.rds
/usr/lib64/R/library/SQUAREM/Meta/features.rds
/usr/lib64/R/library/SQUAREM/Meta/hsearch.rds
/usr/lib64/R/library/SQUAREM/Meta/links.rds
/usr/lib64/R/library/SQUAREM/Meta/nsInfo.rds
/usr/lib64/R/library/SQUAREM/Meta/package.rds
/usr/lib64/R/library/SQUAREM/Meta/vignette.rds
/usr/lib64/R/library/SQUAREM/NAMESPACE
/usr/lib64/R/library/SQUAREM/NEWS
/usr/lib64/R/library/SQUAREM/R/SQUAREM
/usr/lib64/R/library/SQUAREM/R/SQUAREM.rdb
/usr/lib64/R/library/SQUAREM/R/SQUAREM.rdx
/usr/lib64/R/library/SQUAREM/demo/factoranalysis.R
/usr/lib64/R/library/SQUAREM/demo/intcensoring.R
/usr/lib64/R/library/SQUAREM/demo/mmlogistic.R
/usr/lib64/R/library/SQUAREM/demo/poissonmix.R
/usr/lib64/R/library/SQUAREM/demo/squarem.R
/usr/lib64/R/library/SQUAREM/doc/SQUAREM.R
/usr/lib64/R/library/SQUAREM/doc/SQUAREM.Rnw
/usr/lib64/R/library/SQUAREM/doc/SQUAREM.pdf
/usr/lib64/R/library/SQUAREM/doc/index.html
/usr/lib64/R/library/SQUAREM/help/AnIndex
/usr/lib64/R/library/SQUAREM/help/SQUAREM.rdb
/usr/lib64/R/library/SQUAREM/help/SQUAREM.rdx
/usr/lib64/R/library/SQUAREM/help/aliases.rds
/usr/lib64/R/library/SQUAREM/help/paths.rds
/usr/lib64/R/library/SQUAREM/html/00Index.html
/usr/lib64/R/library/SQUAREM/html/R.css
/usr/lib64/R/library/SQUAREM/tests/Hasselblad1969.R
