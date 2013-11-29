%define		fversion	%(echo %{version} |tr r -)
%define		modulename	plyr
Summary:	Tools for splitting, applying and combining data
Name:		R-cran-%{modulename}
Version:	1.8
Release:	1
License:	GPL v2
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	e1c1d2f0c47fd16b2cef6ec9c2e5883c
URL:		http://cran.fhcrc.org/web/packages/plyr/index.html
BuildRequires:	R >= 2.8.1
Requires(post,postun):	R >= 2.8.1
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
plyr is a set of tools that solves a common set of problems: you need
to break a big problem down into manageable pieces, operate on each
pieces and then put all the pieces back together. For example,
you might want to fit a model to each spatial location or time point
in your study, summarise data by panels or collapse high-dimensional
arrays to simpler summary statistics. The development of plyr has been
generously supported by BD (Becton Dickinson).

%prep
%setup -q -c

%build
R CMD build %{modulename} --no-build-vignettes

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}
