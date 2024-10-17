%define major       0
%define libname    %mklibname fastjet %{major}
%define libnamedev  %mklibname -d fastjet
%define develnamestatic %mklibname fastjet -d -s



Name:           fastjet
Version:        3.0.2
Release:        1
License:        GPLv3
Url:		https://www.fastjet.fr
Source0:	http://www.fastjet.fr/repo/%{name}-%{version}.tar.gz
Group:		Sciences/Physics
Summary:        Fast implementation of several recombination jet algorithms
BuildRequires:	gcc-gfortran gcc-c++

%description
A software package for jet finding in pp and e+e- collisions.
It includes fast native implementations of many sequential 
recombination clustering algorithms, plugins for access 
to a range of cone jet finders and tools for advanced jet manipulation. 

%package -n     %{libname}
Summary:        Libraries for %{name}
Group:          System/Libraries
Requires:       %{name}-common
Provides:       %{name} = %{version}-%{release}

%description -n %{libname}
A software package for jet finding in pp and e+e- collisions.
It includes fast native implementations of many sequential 
recombination clustering algorithms, plugins for access 
to a range of cone jet finders and tools for advanced jet manipulation. 


%package -n     %{libnamedev}
Summary:        Libraries and headers for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{libnamedev}
%{libnamedev} contains the libraries and header files needed to
develop programs which make use of %{name}.
The library documentation is available on header files.



%package -n	%{develnamestatic}
License:	BSD-like
Summary:	Library for accessing files in FITS format for C and Fortran
Group:		System/Libraries
Requires:	%{libnamedev} = %version
Requires:	%libname = %version

%description -n %{develnamestatic}
This package contains the headers required for compiling software that uses
the %{name} library


%prep
%setup -q

%build
./configure --enable-allplugins --prefix=%{_prefix} --libdir=%{_libdir}
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}%{_prefix}

find %{buildroot} -type f -name '*.la' -exec rm -f {} \;

%files 
%doc AUTHORS README COPYING
%{_bindir}/%{name}-config

%files -n %{libname}
%{_libdir}/libfastjet.so.%{major}*
%{_libdir}/libfastjetplugins.so.%{major}*
%{_libdir}/libfastjettools.so.%{major}*
%{_libdir}/libsiscone.so.%{major}*
%{_libdir}/libsiscone_spherical.so.%{major}*

%files -n %{libnamedev}
%{_libdir}/libfastjet.so
%{_libdir}/libfastjettools.so
%{_libdir}/libsiscone.so
%{_libdir}/libsiscone_spherical.so
%{_libdir}/libfastjetplugins.so
%{_includedir}/*.h
%{_includedir}/siscone/*.h
%{_includedir}/fastjet/*.h
%{_includedir}/fastjet/*.hh
%{_includedir}/fastjet/tools/*.hh
%{_includedir}/fastjet/internal/*.hh


%files -n %{develnamestatic}
%{_libdir}/*.a

